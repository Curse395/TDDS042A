from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel, field_validator
from enum import Enum

app = FastAPI()


# 1. ENUM
class Course(str, Enum):
    AI = "AI"
    DATA_SCIENCE = "Data_science"
    COMPUTER_SCIENCE = "Computer_science"
    DS = "DS"


# 2. NESTED MODEL
class Address(BaseModel):
    city: str
    state: str
    pincode: str


# 3. STUDENT INPUT MODEL
class Student(BaseModel):
    name: str
    age: int
    email: str
    course: Course
    address: Address

    # Custom validation
    @field_validator("age")
    @classmethod
    def check_age(cls, age):
        if age < 18 or age > 60:
            raise ValueError("Age must be between 18 and 60")

        return age


# 4. RESPONSE MODEL
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str
    course: Course
    address: Address


students = []
next_id = 1


# Dependency Injection
def get_current_user():
    return "Admin"


# CREATE STUDENT
@app.post(
    "/students",
    response_model=StudentResponse
)
def create_student(student: Student):

    global next_id

    new_student = {
        "id": next_id,
        "name": student.name,
        "age": student.age,
        "email": student.email,
        "course": student.course,
        "address": student.address
    }

    students.append(new_student)
    next_id += 1

    return new_student


# GET ALL STUDENTS
@app.get("/students")
def get_students():
    return students


# GET SINGLE STUDENT
@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:

        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# UPDATE STUDENT
@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    student_data: Student
):

    for student in students:

        if student["id"] == student_id:

            student["name"] = student_data.name
            student["age"] = student_data.age
            student["email"] = student_data.email
            student["course"] = student_data.course
            student["address"] = student_data.address

            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# DELETE STUDENT
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# ASYNC DEMO
@app.get("/async-demo")
async def async_demo():

    return {
        "message": "This is an asynchronous FastAPI endpoint"
    }


# BACKGROUND TASK
def write_notification(student_id):

    with open("notifications.txt", "a") as file:

        file.write(
            f"Notification sent to student {student_id}\n"
        )


@app.post("/students/{student_id}/notify")
def notify_student(
    student_id: int,
    background_tasks: BackgroundTasks
):

    # Check whether student exists
    for student in students:

        if student["id"] == student_id:

            background_tasks.add_task(
                write_notification,
                student_id
            )

            return {
                "message": "Notification task added"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# DEPENDENCY INJECTION
@app.get("/profile")
def profile(
    user=Depends(get_current_user)
):

    return {
        "message": "Dependency Injection Example",
        "current_user": user
    }
