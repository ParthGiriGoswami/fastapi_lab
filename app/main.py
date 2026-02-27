from fastapi import FastAPI  as api
from routers import health
app = api()
app.include_router(health.route)
@app.get("/")
def read_root():
    return {"message": "Hello World, FastAPI is running!"}