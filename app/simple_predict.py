def predict_from_gpa(data):
    if data.gpa < 2.5 or data.attendance < 60 or data.assignments_completed < 60:
        return "Dropout Risk"
    elif data.hours_studied < 10 and not data.financial_aid:
        return "At Risk – Needs Monitoring"
    else:
        return "No Risk"
