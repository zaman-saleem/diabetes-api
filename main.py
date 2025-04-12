from fastapi import FastAPI
app = FastAPI()
@app.get("/users")
def index():
    return {
        "message": "Users get successfully",
        "data": {
                "id": 1,
                "name": "<NAME>"
            }

    }

@app.get("/items/{item_id}")
def index(item_id: int):
    return{"product_id": item_id}