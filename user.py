from fastapi import FastAPI

app = FastAPI()

employees = {}

@app.get("/")
def home():
    return {"message": "Hello world"}

@app.post("/employees")
def create_employee(emp_id: int, emp_name: str, emp_age: int, emp_department: str):
    employees[emp_id] = {"name": emp_name, "age": emp_age, "department": emp_department}
    return {"Employees added successfully!"}

@app.get("/employees")
def get_all_employees():
    return employees

@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    if emp_id in employees:
        return {"employee": employees[emp_id]}
    return {"error": "Employee not found"}

@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, emp_name: str, emp_age: int, emp_department: str):
    if emp_id not in employees:
        return {"error": "Employee not found"}

    employees[emp_id] = {"name": emp_name, "age": emp_age, "department": emp_department}
    return {"message": "Employee updated successfully!"}

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    if emp_id not in employees:
     del employees[emp_id]
    return {"Employee deleted successfully!"}















