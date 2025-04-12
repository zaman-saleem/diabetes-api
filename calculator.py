from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Calculator API"}

@app.get("/calculate")
def calculate(a: float, b: float):
    addition = a + b
    subtraction = a - b
    return {
        "Number 1": a,
        "Number 2": b,
        "Addition": addition,
        "Subtraction": subtraction
    }
