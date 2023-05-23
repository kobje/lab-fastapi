from pydantic import BaseModel

class StudentCreateSchema(BaseModel):
    student_id: int
    first_name: str
    last_name: str

class StudentUpdateSchema(BaseModel):
    first_name: str
    last_name: str

students = []