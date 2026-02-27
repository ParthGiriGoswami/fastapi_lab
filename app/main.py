from fastapi import FastAPI
from app.routers import health
app = FastAPI()
app.include_router(health.route)
@app.get("/")
def read_root():
    return {"message": "Hello World, FastAPI is working!"}