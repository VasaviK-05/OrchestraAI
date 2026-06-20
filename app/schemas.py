
from pydantic import BaseModel, Field


class JobRequest(BaseModel):

    priority: int = Field(
        ge=1,
        le=3
    )

    model_type: str
    payload: dict