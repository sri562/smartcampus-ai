import streamlit as st
import requests

st.set_page_config(page_title="SmartCampus AI", layout="centered")
st.title("SmartCampus AI – Dropout Risk Predictor")

student_data = {
    "gpa": st.slider("GPA", 0.0, 4.0, 2.5),
    "attendance": st.slider("Attendance (%)", 0, 100, 75),
    "assignments_completed": st.slider("Assignments Completed", 0, 100, 70),
    "hours_studied": st.slider("Hours Studied per Week", 0, 40, 10),
    "financial_aid": st.selectbox("Financial Aid?", ["Yes", "No"])
}

if st.button("Predict Dropout Risk"):
    student_data["financial_aid"] = 1 if student_data["financial_aid"] == "Yes" else 0

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=student_data)
        result = response.json()

        if "prediction" in result:
            st.success(f"Prediction: {result['prediction']}")
        else:
            st.warning("FastAPI did not return a valid prediction.")

        if "gpt_advice" in result and result["gpt_advice"]:
            st.info(f"Advice:\n\n{result['gpt_advice']}")
    except Exception as e:
        st.error("Error connecting to FastAPI backend.")
        st.text(str(e))
