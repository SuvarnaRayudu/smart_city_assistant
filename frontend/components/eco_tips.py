import streamlit as st
import requests

def render():
    st.subheader("Eco Tips Generator")
    topic = st.text_input("Enter topic (e.g. plastic, solar, water)")

    if st.button("Generate Tips"):
        res = requests.get(f"http://localhost:8000/eco/tips?topic={topic}")
        st.code(res.json()["tips"])
