from fastapi import FastAPI
from app.schemas import JobRequest

app = FastAPI(
    title="OrchestraAI",
    version="0.1.0"
)


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


@app.post("/jobs")
def submit_job(job: JobRequest):
    return {
        "status": "accepted",
        "job": job
    }