from fastapi import APIRouter  
route = APIRouter()
@route.get("/health")
def health_check():
    return {"status": "ok"}