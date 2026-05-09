from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "DevOps API is running"}

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}
