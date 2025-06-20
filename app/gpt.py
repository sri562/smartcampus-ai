def generate_advice(student: dict, prediction: str) -> str:
    if prediction == "No Risk":
        return "Keep up the good work! Maintain consistency in GPA and attendance."
    else:
        tips = []
        if student["gpa"] < 2.5:
            tips.append("Focus on improving your GPA.")
        if student["attendance"] < 75:
            tips.append("Increase class attendance.")
        if student["assignments_completed"] < 70:
            tips.append("Complete more assignments on time.")
        if student["hours_studied"] < 20:
            tips.append("Increase weekly study hours.")
        if student["financial_aid"] == 0:
            tips.append("Consider applying for financial aid.")
        return " ".join(tips) if tips else "Reach out to an academic advisor for personalized support."
