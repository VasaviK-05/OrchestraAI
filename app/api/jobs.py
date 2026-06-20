import time
import uuid

from fastapi import APIRouter
from app.models.job import JobRequest
from app.core.queue import job_queue

router = APIRouter()

@router.post("/jobs")
def submit_job(request: JobRequest):

    job = {
        "job_id": str(uuid.uuid4()),
        "priority": request.priority,
        "model_type": request.model_type,
        "payload": request.payload,
        "timestamp": time.time()
    }

    job_queue.put(
        (request.priority, job)
    )

    return {
        "status": "accepted",
        "job_id": job["job_id"]
    }


@router.get("/queue-size")
def queue_size():
    return {
        "jobs_waiting": job_queue.qsize()
    }