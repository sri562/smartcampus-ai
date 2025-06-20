from fastapi import FastAPI
from app.schemas import FlexibleStudentData
from app.predict import predict_dropout
from app.gpt import generate_advice

app = FastAPI(
    title="SmartCampus AI API",
    description="Predicts student dropout risk and provides GPT-style advice.",
    version="1.0"
)

@app.get("/")
def root():
    return {"message": "SmartCampus AI is running!"}

@app.post("/predict")
def predict(data: FlexibleStudentData):
    student_dict = data.dict()
    prediction = predict_dropout(student_dict)
    advice = generate_advice(student_dict, prediction)
    return {
        "prediction": prediction,
        "gpt_advice": advice
    }
