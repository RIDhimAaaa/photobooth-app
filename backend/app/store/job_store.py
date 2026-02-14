from typing import Dict
from uuid import UUID

from app.models.job import Job


class JobStore:
    def __init__(self) -> None:
        self._jobs: Dict[UUID, Job] = {}

    def save(self, job: Job) -> None:
        self._jobs[job.id] = job

    def get(self, job_id: UUID) -> Job | None:
        return self._jobs.get(job_id)

    def get_by_session(self, session_id: UUID) -> list[Job]:
        return [
            job for job in self._jobs.values()
            if job.session_id == session_id
        ]
