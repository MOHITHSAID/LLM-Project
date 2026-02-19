import streamlit as st
from vision.inference import predict_image
from agent.gemini_agent import run_agent

st.title("AI Monument Travel Guide")

uploaded_file = st.file_uploader("Upload a monument image", type=["jpg", "jpeg", "png"])

user_question = st.text_input("Ask something about this monument (hotels, transport, traffic):")

if uploaded_file is not None:

    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())

    monument, confidence = predict_image("temp.jpg")

    st.subheader("Prediction")
    st.write(f"{monument} (Confidence: {confidence:.2f})")

    if confidence > 0.6:

        if st.button("Get Information"):
            response = run_agent(monument, user_question)
            st.subheader("Response")
            st.write(response)

    else:
        st.warning("Model not confident enough.")
