from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class JobCreateResponse(BaseModel):
    job_id: UUID
    status: str
    created_at: datetime


class JobStatusResponse(BaseModel):
    job_id: UUID
    status: str
    created_at: datetime
    completed_at: datetime | None
