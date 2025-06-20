def generate_advice(data: dict, prediction: str) -> str:
    if prediction == "Dropout Risk":
        return "This student is at risk. Consider reaching out with academic and financial support options."
    else:
        return "The student appears to be in good standing. Encourage continued engagement and performance."
