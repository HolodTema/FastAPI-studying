import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4())


#simple database parody 
people = [Person("Tom", 38), Person("Bob", 42), Person("Sam", 28)]

#to find user in people list
def find_person(id):
    for person in people:
        if person.id==id:
            return person
    return None


#create fastAPI obj
app = FastAPI()

@app.get("/")
async def main():
    return FileResponse("public/index.html")

@app.get("/api/users")
def get_people():
    return people

@app.get("/api/users/{id}")
def get_person(id):
    person = find_person(id)
    if person==None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content = {
                "message": "User not found."
            }
        )
    return person


@app.post("/api/users")
def create_person(data = Body()):
    person = Person(data["name"], data["age"])
    people += [person]
    return person

@app.put("/api/users")
def edit_person(data = Body()):
    person = find_person(data["id"])
    if person==None:
        return JSONResponse(
            status_code = status.HTTP_404_NOT_FOUND,
            content = {
                "message": "User not found."
            }
        )
    person.name = data["name"]
    person.age = data["age"]
    return person

@app.delete("/api/users")
def delete_person(id):
    person = find_person(id)
    if person==None:
        return JSONResponse(
            status_code = status.HTTP_404_NOT_FOUND,
            content = {
                "message": "User not found."
            }
        )
    people.remove(person)
    return person



