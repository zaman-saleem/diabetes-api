from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Hello"}

@app.get("/blog")                             #fetch all blog use
def index():
    return {'data':'blog list'}

@app.get("/blog/{blog_id}")               #fetch single blog
def show(blog_id: int):
    return {'data':blog_id}

@app.get("/blog/{blog_id}/comments")      #fetch comment of blog with id = id
def comments(blog_id):
    return {'data': {'successful'}}

@app.post("/blog")
def create_blog():
    return {'data': 'Blog is created'}







