import streamlit as st
import pandas as pd
import requests

def render():
    st.subheader("📊 KPI Forecast (Water, Energy, etc.)")
    file = st.file_uploader("Upload KPI CSV", type="csv")

    if file and st.button("Forecast"):
        res = requests.post("http://localhost:8000/kpi/forecast", files={"file": file})
        data = res.json()
        st.metric(label=f"📈 Forecast for {data['next_year']}", value=round(data['forecast'], 2))
