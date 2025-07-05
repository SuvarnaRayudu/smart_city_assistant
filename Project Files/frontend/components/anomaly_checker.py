import streamlit as st
import requests
import pandas as pd

def render():
    st.subheader("Upload Usage Data for Anomaly Detection")
    file = st.file_uploader("Upload CSV", type="csv")

    if file and st.button("Check Anomalies"):
        res = requests.post("http://localhost:8000/anomaly/", files={"file": file})
        anomalies = res.json()["anomalies"]
        st.write("Detected Anomalies:")
        st.dataframe(pd.DataFrame(anomalies))
