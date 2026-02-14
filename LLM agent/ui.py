import streamlit as st
from agent_core import agent_decision
from tool_executor import execute_tool
from response_formatter import format_response

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="AI Monument Travel Assistant",
    layout="centered"
)

st.title("🏛️ AI Monument Travel Assistant")
st.write("Select what you want to know about the monument")

# ---------------------------
# Monument Input
# ---------------------------
monument = st.text_input(
    "Monument Name",
    value="Taj Mahal"
)

# ---------------------------
# Question Type Selection
# ---------------------------
question_type = st.selectbox(
    "Choose a category",
    [
        "Select an option",
        "Hotels & Stay",
        "Budget Stay",
        "Restaurants & Food",
        "Budget Food",
        "Cheapest Travel",
        "Local Transport",
        "Flights",
        "General Information",
        "Custom Question"
    ]
)

# ---------------------------
# Map selection to query
# ---------------------------
query_map = {
    "Hotels & Stay": "Suggest nearby hotels",
    "Budget Stay": "Suggest cheap budget stays",
    "Restaurants & Food": "Suggest nearby restaurants and food",
    "Budget Food": "Suggest cheap food options",
    "Cheapest Travel": "What is the cheapest way to reach?",
    "Local Transport": "What local transport is available?",
    "Flights": "Show flight options",
    "General Information": "Tell me about this monument"
}

user_query = ""

if question_type == "Custom Question":
    user_query = st.text_input(
        "Enter your custom question",
        placeholder="Type anything..."
    )
elif question_type in query_map:
    user_query = query_map[question_type]

# ---------------------------
# Ask Button
# ---------------------------
if st.button("Ask Assistant"):
    if not monument.strip():
        st.warning("Please enter a monument name.")
    elif question_type == "Select an option":
        st.warning("Please choose a category.")
    elif question_type == "Custom Question" and not user_query.strip():
        st.warning("Please type your question.")
    else:
        with st.spinner("Thinking..."):
            agent_result = agent_decision(monument, user_query)

            if agent_result["type"] == "tool_call":
                tool_result = execute_tool(agent_result)
                final_answer = format_response(agent_result, tool_result)
            else:
                final_answer = format_response(agent_result)

        # ---------------------------
        # Display Results
        # ---------------------------
        st.subheader("📢 Result")
        st.success(final_answer)

        with st.expander("🧠 Agent Decision (Debug View)"):
            st.json(agent_result)
