from google import genai
from rag.retriever import retrieve
from mcp_client import call_tool
import json
import re

# 🔴 IMPORTANT: Replace with your new regenerated API key
client = genai.Client(api_key="AIzaSyBCU14cbEn-sXuvPs6Ts_pS_meX6qRfvuo")


def run_agent(monument_name, user_question=None):

    # 1️⃣ Combine monument + user question
    if user_question:
        query = f"{user_question} about {monument_name}"
    else:
        query = monument_name

    # 2️⃣ Retrieve RAG context
    context = retrieve(monument_name)

    # 3️⃣ Decision prompt for Gemini
    decision_prompt = f"""
    You are a travel assistant.

    Monument: {monument_name}

    Context:
    {context}

    User Question:
    {query}

    If user asks for hotels, respond ONLY in JSON:
    {{
        "tool": "get_hotels",
        "arguments": {{"location": "CityName"}}
    }}

    If user asks for transport, respond ONLY in JSON:
    {{
        "tool": "get_transport",
        "arguments": {{"source": "City", "destination": "City"}}
    }}

    If user asks about traffic, respond ONLY in JSON:
    {{
        "tool": "get_traffic",
        "arguments": {{"location": "CityName"}}
    }}

    If no tool is needed, answer normally.
    """

    # 4️⃣ Get Gemini response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=decision_prompt
    )

    text = response.text.strip()

    print("\n--- RAW GEMINI RESPONSE ---")
    print(text)
    print("----------------------------\n")

    # 5️⃣ Detect tool call
    if '"tool"' in text:

        try:
            # Remove markdown formatting if present
            cleaned = text.strip()
            cleaned = re.sub(r"```json", "", cleaned)
            cleaned = re.sub(r"```", "", cleaned)

            # Extract JSON object
            json_match = re.search(r'\{.*\}', cleaned, re.DOTALL)

            if not json_match:
                print("No valid JSON found.")
                return "Tool call parsing failed."

            json_text = json_match.group()

            tool_data = json.loads(json_text)

            tool_name = tool_data["tool"].strip()
            args = tool_data["arguments"]

            # 6️⃣ Call MCP tool
            tool_result = call_tool(tool_name, args)

            # 7️⃣ Send tool result back to Gemini for formatting
            final_prompt = f"""
            Tool result:
            {tool_result}

            Convert this into a clean and user-friendly response.
            """

            final_response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=final_prompt
            )

            return final_response.text

        except Exception as e:
            print("Parsing error:", e)
            print("RAW TEXT:", text)
            return "Tool call parsing failed."

    # 8️⃣ If no tool call → return direct answer
    return text
