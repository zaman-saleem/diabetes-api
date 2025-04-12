from fastapi import FastAPI

app = FastAPI()
tasks = {}
@app.get("/")
def home():
    return {"message":"Welcome to project.!"}

@app.post("/tasks")
def create_task(task_id: int, task_name: str, task_status: str):
    tasks[task_id] = {"name": task_name, "status": task_status}
    return {"message": "Tasks created successfully!"}

@app.get("/tasks")
def get_all_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks:
        return tasks[task_id]
    return {"message": "Task exists!"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_name: str, task_status: str = None):
    if task_id not in tasks:
        return{"message": "Task does not exists!"}
    if task_name:
        tasks[task_id]["name"] = task_name
        if task_status:
            tasks[task_id]["status"] = task_status
            return {"message": "Task updated successfully!"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        return{"message": "Task not found"}
    del tasks[task_id]
    return {"message": "Task deleted successfully!"}




