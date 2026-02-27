from fastapi import FastAPI
from app.routers import health, users
app = FastAPI()
app.include_router(health.route)
app.include_router(users.route)
@app.get("/")
def read_root():
    return {"message": "Hello World, FastAPI is working!"}