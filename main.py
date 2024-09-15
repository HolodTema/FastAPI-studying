from fastapi import FastAPI, Response, Path

app = FastAPI()




# @app.get("/notfound", status_code=404) 
# def notfound():
#   return {"message": "Resource not found."}

@app.get("users/{id}", status_code=200)
def users(response: Response, id: int = Path()):
    if id<1:
        response.status_code = 400
        return {"message": "Incorrect data"}
    return {"message": f"id = {id}"}

