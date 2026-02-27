from fastapi import AppRouter as router
route=router()
@route.get("/health")
def health_check():
    return {"status": "ok"}