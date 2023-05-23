from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudentCreateSchema(BaseModel):
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