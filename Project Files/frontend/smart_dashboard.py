import streamlit as st
from streamlit_option_menu import option_menu
from components import (
    chat_assistant, feedback_form, eco_tips,
    summary_card, kpi_dashboard, anomaly_checker, policy_summarizer
)

st.set_page_config(page_title="Smart City Assistant", layout="wide")
st.markdown("<h1 style='text-align: center;'>🌆 Sustainable Smart City Assistant</h1>", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Chat Assistant", "Eco Tips", "Policy Summarizer", "KPI Forecast", "Anomaly Check", "Citizen Feedback"],
        icons=["robot", "leaf", "file-earmark-text", "bar-chart-line", "exclamation-triangle", "pencil-square"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Chat Assistant":
    chat_assistant.render()
elif selected == "Eco Tips":
    eco_tips.render()
elif selected == "Policy Summarizer":
    policy_summarizer.render()
elif selected == "KPI Forecast":
    kpi_dashboard.render()
elif selected == "Anomaly Check":
    anomaly_checker.render()
elif selected == "Citizen Feedback":
    feedback_form.render()
