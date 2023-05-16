from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/students")
async def createStudent(student: StudentCreateSchema):
    return student