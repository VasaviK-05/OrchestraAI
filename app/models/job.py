from pydantic import BaseModel, Field
from uuid import UUID
from typing import Dict, Any

class JobRequest(BaseModel):
    priority: int = Field(ge=1, le=3)
    model_type: str
    payload: Dict[str, Any]


class Job(BaseModel):
    job_id: UUID
    priority: int
    model_type: str
    payload: Dict[str, Any]
    timestamp: float