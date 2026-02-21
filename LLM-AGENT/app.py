# app.py

import streamlit as st
from agent import run_agent

st.set_page_config(
    page_title="AI Monument & Travel Assistant",
    layout="centered"
)

st.title("🏛️ AI Monument & Travel Assistant")

# Step 1: User enters monument
monument_name = st.text_input("Enter Monument or Location:")

# Only show question box once monument is entered
if monument_name:
    user_question = st.text_input("Ask anything about this place:")

    if st.button("Ask") and user_question.strip() != "":
        with st.spinner("Thinking..."):
            answer = run_agent(monument_name, user_question)
            st.markdown(f"**Assistant:** {answer}")