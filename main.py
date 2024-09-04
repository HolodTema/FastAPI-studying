from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


# @app.get("/")
# def root():
# 	return FileResponse("index.html")

# @app.get("/file", response_class = FileResponse)
# def root_html():
# 	return "index.html"
	
@app.get("/")
def root():
	return FileResponse("index.html", filename="mainpage.html", media_type="application/octet-stream")

