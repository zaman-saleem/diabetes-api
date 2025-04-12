from fastapi import FastAPI
from typing import Optional
app = FastAPI()
students = {}
@app.post("/add-student/{student_id}")
def add_student(student_id: int, name: str, age: int, grade: str):
    students[student_id] = {"name": name, "age": age,"grade":grade}
    return {"message": "Student added!", "students": students}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students.get(student_id, {"error": "Student not found"})


@app.get("/get-all-students/")
def get_all_students(age: Optional[int] = None, grade: Optional[str] = None):
    if age:
        filtered_students = {x: y for x, y in students.items() if y["age"] == age}
        return {"filtered_students": filtered_students}

    if grade:
        filtered_students = {x: y for x, y in students.items() if y["grade"] == grade}
        return {"filtered_students": filtered_students}

    return {"students": students}