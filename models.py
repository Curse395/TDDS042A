from pydantic import BaseModel

class student(BaseModel):
    student_id: int
    name: str
    age: int
    course: str
    year: int