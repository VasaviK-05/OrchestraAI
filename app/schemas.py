from pydantic import BaseModel
from typing import Dict, Any


class JobRequest(BaseModel):
    priority: int
    model_type: str
    payload: Dict[str, Any]