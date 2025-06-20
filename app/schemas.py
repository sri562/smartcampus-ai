# app/schemas.py

from pydantic import BaseModel, Field

class StudentData(BaseModel):
    tuition_fees_up_to_date: int
    curricular_units_2nd_sem_approved: int
    scholarship_holder: int
    curricular_units_2nd_sem_enrolled: int
    curricular_units_1st_sem_approved: int
    curricular_units_2nd_sem_evaluations: int
    curricular_units_1st_sem_evaluations: int
    debtor: int
    mothers_occupation: int
    curricular_units_1st_sem_enrolled: int
    age_at_enrollment: int
    course: int
    gdp: float
    curricular_units_2nd_sem_without_evaluations: int
    previous_qualification: int
    curricular_units_1st_sem_without_evaluations: int
    unemployment_rate: float
    application_mode: int
    admission_grade: float
    curricular_units_1st_sem_grade: float


class FlexibleStudentData(BaseModel):
    gpa: float = Field(..., ge=0.0, le=4.0)
    attendance: int = Field(..., ge=0, le=100)
    assignments_completed: int = Field(..., ge=0, le=100)
    hours_studied: int = Field(..., ge=0, le=60)
    financial_aid: int = Field(..., ge=0, le=1)

