import streamlit as st
import requests

st.set_page_config(page_title="SmartCampus AI Dashboard", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🎓 SmartCampus AI Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown("---")

with st.form(key="student_form"):
    col1, col2 = st.columns(2)
    with col1:
        gpa = st.slider("📘 GPA", 0.0, 4.0, 3.0, 0.1)
        attendance = st.slider("🧑‍🏫 Attendance (%)", 0, 100, 85)
        assignments_completed = st.slider("📑 Assignments Completed (%)", 0, 100, 90)
    with col2:
        hours_studied = st.slider("⏱️ Hours Studied per Week", 0, 60, 25)
        financial_aid = st.selectbox("💰 Financial Aid Received?", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

    submit_button = st.form_submit_button(label="🔍 Predict Dropout Risk")

if submit_button:
    student_data = {
        "gpa": gpa,
        "attendance": attendance,
        "assignments_completed": assignments_completed,
        "hours_studied": hours_studied,
        "financial_aid": financial_aid
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=student_data)
        result = response.json()

        st.markdown("---")
        if result["prediction"] == "Dropout Risk":
            st.error(f"🚨 **Prediction: {result['prediction']}**")
            st.warning(f"💡 GPT Advice: {result['gpt_advice']}")
        else:
            st.success(f"✅ **Prediction: {result['prediction']}**")
            st.info(f"🎯 GPT Advice: {result['gpt_advice']}")
    except Exception as e:
        st.error("⚠️ Unable to connect to the FastAPI server.")
        st.text(f"Details: {e}")
