from fastapi import FastAPI

from app.api.sessions import router as session_router
from app.api.jobs import router as job_router   # ADD THIS

app = FastAPI(title="Photobooth Backend")

app.include_router(session_router)
app.include_router(job_router)   # ADD THIS

@app.get("/health")
def health():
    return {"status": "ok"}
