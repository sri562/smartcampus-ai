from google.generativeai import list_models
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

for m in list_models():
    print(m.name)
