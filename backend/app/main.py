from fastapi import FastAPI

from app.api.sessions import router as session_router

app = FastAPI(title="Photobooth Backend")

app.include_router(session_router)


@app.get("/health")
def health():
    return {"status": "ok"}

