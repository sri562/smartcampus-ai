import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "tuition_fees_up_to_date": 0,
    "curricular_units_2nd_sem_approved": 0,
    "scholarship_holder": 0,
    "curricular_units_2nd_sem_enrolled": 6,
    "curricular_units_1st_sem_approved": 0,
    "curricular_units_2nd_sem_evaluations": 7,
    "curricular_units_1st_sem_evaluations": 5,
    "debtor": 1,
    "mothers_occupation": 0,
    "curricular_units_1st_sem_enrolled": 6,
    "age_at_enrollment": 28,
    "course": 9070,
    "gdp": 0.9,
    "curricular_units_2nd_sem_without_evaluations": 2,
    "previous_qualification": 1,
    "curricular_units_1st_sem_without_evaluations": 2,
    "unemployment_rate": 1.4,
    "application_mode": 1,
    "admission_grade": 80.0,
    "curricular_units_1st_sem_grade": 8.5,
    "gpa": 3.2,
    "attendance": 85,
    "assignments_completed": 88,
    "hours_studied": 34,
    "financial_aid": 1
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Raw Text:", response.text)

try:
    print("JSON Response:", response.json())
except Exception as e:
    print("Failed to decode JSON:", e)
