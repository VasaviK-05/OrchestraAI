from fastapi import FastAPI
from app.schemas import JobRequest
from app.api.jobs import router as jobs_router

app = FastAPI(
    title="OrchestraAI",
    version="0.1.0"
)

app.include_router(jobs_router)

@app.get("/")
def root():
    return {
        "message": "OrchestraAI Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }