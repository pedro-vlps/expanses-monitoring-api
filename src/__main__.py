"""Main file for the API application."""
from fastapi import FastAPI
# from api_crud_generate_libary.routers import router

app = FastAPI()

@app.get("/healthy")
def healthy():
    """Route to check if the API is online."""
    return {"status": "ok"}
