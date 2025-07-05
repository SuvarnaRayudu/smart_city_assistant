import streamlit as st
import requests

def render():
    st.subheader("Submit Feedback")
    name = st.text_input("Your Name")
    category = st.selectbox("Category", ["Water", "Electricity", "Roads", "Garbage", "Other"])
    message = st.text_area("Message")

    if st.button("Submit"):
        res = requests.post("http://localhost:8000/feedback/", json={
            "name": name,
            "category": category,
            "message": message
        })
        st.success(res.json()["message"])
