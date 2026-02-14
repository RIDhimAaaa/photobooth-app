from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from enum import Enum


class JobStatus(str, Enum):
    CREATED = "created"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Job:
    id: UUID
    session_id: UUID
    status: JobStatus
    created_at: datetime
    completed_at: datetime | None = None
