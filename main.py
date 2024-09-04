from fastapi import FastAPI, Query, Path


app = FastAPI()


# @app.get("/users")
# def get_model(name:str, age:int):
# 	return {"user_name": name, "user_age": age}

# @app.get("/users")
# def users(name:str = Query(min_length=3, max_length=20)):
# 	return {"name": name}

# @app.get("/users")
# def users(name:str = Query(min_length=3, max_length=20), 
# 			age:int = Query(ge=18, lt=111)):
# 	return {"name": name, "age": age}

# @app.get("/users")
# def users(people: list[str] = Query()):
# 	return {"people": people}

@app.get("/users/{name}")
def users(name:str = Path(min_length=3, max_length=20),
			age:int = Query(ge=18, lt=111)):
	return {"name": name, "age": age}
