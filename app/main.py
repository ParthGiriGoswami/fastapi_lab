from fastapi import FastAPI  as api
app = api()
@app.get("/")
def read_root():
    return {"message": "Hello World, FastAPI is running!"}