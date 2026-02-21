# agent.py

from llm_client import client
from prompt import SYSTEM_PROMPT

def run_agent(monument_name: str, user_query: str) -> str:
    """
    Pure prompt-based Gemini agent using gemini-2.5-flash
    """

    full_prompt = f"""
{SYSTEM_PROMPT}

Location / Monument:
{monument_name}

User Question:
{user_query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    return response.text