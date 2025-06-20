import numpy as np

def predict_dropout(student_dict: dict) -> str:
    # Dummy model logic based on admission grade
    grade = student_dict.get("admission_grade", 0)
    if grade < 60:
        return "Dropout Risk"
    else:
        return "No Risk"

def predict_dropout(student: dict) -> str:
    # Normalize features to 0–1
    gpa_score = student["gpa"] / 4.0
    attendance_score = student["attendance"] / 100.0
    assignments_score = student["assignments_completed"] / 100.0
    hours_score = student["hours_studied"] / 60.0
    aid_score = student["financial_aid"]

    # Weighted score
    score = (
        gpa_score * 0.4 +
        attendance_score * 0.2 +
        assignments_score * 0.2 +
        hours_score * 0.1 +
        aid_score * 0.1
    )

    return "No Risk" if score >= 0.6 else "Dropout Risk"

