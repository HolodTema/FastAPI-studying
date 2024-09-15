from pydantic import BaseModel, Field
from fastapi import FastAPI
from fastapi.responses import FileResponse


class Person(BaseModel): 
    name: str = Field(default="Undefined", min_length=3, max_length=30)
    age: int = Field(default = "18", ge=18, lt=111)

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index.html")

@app.post("/hello")
def hello(people: list[Person]):
    return {"message": people}

