from app.store.job_store import JobStore
from app.services.job_service import JobService


# single shared instances
job_store = JobStore()
job_service = JobService(job_store)
