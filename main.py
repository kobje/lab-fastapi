from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudentCreateSchema(BaseModel):
    student_id: int
    first_name: str
    last_name: str

class StudentUpdateSchema(BaseModel):
    first_name: str
    last_name: str

students = []

@app.post("/students")
async def createStudent(student: StudentCreateSchema):
    students.append(student)
    return student
@app.get("/")
async def root():
    return students
@app.get("/student/<id>")
async def get_student(id: int):
    for student in students:
        if student.student_id == id:
            return student
@app.post("/student/<id>")
async def update_student(id: int, updated_student: StudentUpdateSchema):
    for student in students:
        if student.student_id == id:
            student.first_name = updated_student.first_name
            student.last_name = updated_student.last_name