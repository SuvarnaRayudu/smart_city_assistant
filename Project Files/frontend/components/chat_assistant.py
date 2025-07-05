import streamlit as st
import requests

def render():
    st.subheader("🤖 Ask the Smart City Assistant")
    prompt = st.text_input("Enter your question")

    if st.button("Ask"):
        with st.spinner("Thinking..."):
            res = requests.post("http://localhost:8000/chat/", json={"prompt": prompt})
            st.success(res.json()["response"])
