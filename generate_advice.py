import google.generativeai as genai
import os

# Gemini API Key
genai.configure(api_key="AIzaSyD0dsDsjFTWk36mWwaTQ6FdH0WZvIl7pzg")

def get_gpt_advice(student_features: dict) -> str:
    try:
        prompt = f"Based on the following student data, give academic and financial advice:\n\n{student_features}"
        model = genai.GenerativeModel("gemini-1.5-flash")  # Fast + latest model
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"GPT error: {str(e)}"
