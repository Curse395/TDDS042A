from fastapi import FastAPI
from models import student

app = FastAPI()

students = [
    {"student_id": 1, "name": "Zahir", "age": 20,"course":"BSC Data Science","year":3},
    {"student_id": 2, "name": "Aryan", "age": 22,"course":"BSC AI","year":3}]

@app.get("/students")
def get_students():
    return students

@app.post("/create-student")
def create_student(new_student: student):
    students.append(new_student)
    return new_student

@app.delete("/delete_student/{student_id}")
def delete_student(student_id:int):
    if student_id in students:
        deleted=student.pop(student_id)
        
        return {"message":"Student Delted",
                "student":deleted}
        return {"error":"Student Not Found"}

@app.put("/update_student/{student_id}")
def update_student(student_id: int, updated_student: student):
    students[0] = updated_student.model_dump()
    return students[0]