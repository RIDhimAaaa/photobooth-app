from fastapi import APIRouter
from uuid import UUID
from fastapi import HTTPException

from app.services.job_service import JobService
from app.store.job_store import JobStore
from app.api.schemas.job import JobCreateResponse, JobStatusResponse
from app.dependencies import job_store, job_service


router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.post("/", response_model=JobCreateResponse)
def create_job(session_id: UUID):

    job = job_service.create_job(session_id=session_id)

    return JobCreateResponse(
        job_id=job.id,
        status=job.status,
        created_at=job.created_at,
    )


@router.get("/{job_id}", response_model=JobStatusResponse)
def get_job(job_id: UUID):

    job = job_service.get_job(job_id)

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return JobStatusResponse(
        job_id=job.id,
        status=job.status,
        created_at=job.created_at,
        completed_at=job.completed_at,
    )
