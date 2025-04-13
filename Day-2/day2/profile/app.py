from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/assets",StaticFiles(directory="assets"), name ="assets")

def profile_html():
    with open("templates/index.html", "r") as html_file:
        content = html_file.read()
    return HTMLResponse(content=content,status_code=200)

@app.get("/", response_class=HTMLResponse)


def home():
    return profile_html()


