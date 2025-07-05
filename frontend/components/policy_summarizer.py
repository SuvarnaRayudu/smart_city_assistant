import streamlit as st
import requests

def render():
    st.subheader("Upload Policy Document for Summarization")
    file = st.file_uploader("Upload a .txt file", type=["txt"])

    if file and st.button("Summarize"):
        with st.spinner("Summarizing..."):
            res = requests.post(
                "http://localhost:8000/policy/summarize",
                files={"file": file}
            )
            st.success("Summary:")
            st.markdown(res.json()["summary"])

    st.subheader("🔍 Semantic Policy Search")
    search_query = st.text_input("Search policies semantically")

    if st.button("Search Policies"):
        res = requests.get(f"http://localhost:8000/vector/search?query={search_query}")
        for i, chunk in enumerate(res.json()["results"]):
            st.markdown(f"**Result {i+1}:**")
            st.info(chunk)