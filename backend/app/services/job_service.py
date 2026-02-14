import time
from datetime import datetime
from threading import Thread
from uuid import UUID, uuid4

from app.models.job import Job, JobStatus
from app.store.job_store import JobStore


class JobService:

    def __init__(self, store: JobStore) -> None:
        self.store = store

    def create_job(self, session_id: UUID) -> Job:

        job = Job(
            id=uuid4(),
            session_id=session_id,
            status=JobStatus.CREATED,
            created_at=datetime.utcnow(),
            completed_at=None,
        )

        print(f"[MAIN] Created job {job.id}")

        self.store.save(job)

        # Start background processing
        self._start_background_worker(job.id)

        return job

    def get_job(self, job_id: UUID) -> Job | None:
        return self.store.get(job_id)

    def _start_background_worker(self, job_id: UUID):

        def worker():

            print(f"[WORKER] Started worker for job {job_id}")

            job = self.store.get(job_id)

            if job is None:
                print("[WORKER] ERROR: Job not found")
                return

            # Immediately set to processing
            job.status = JobStatus.PROCESSING
            print(f"[WORKER] Job {job_id} → PROCESSING")

            # simulate processing
            time.sleep(5)

            job.status = JobStatus.COMPLETED
            job.completed_at = datetime.utcnow()

            self.store.save(job)
            print(f"[WORKER] Job {job_id} → COMPLETED")

        thread = Thread(target=worker)
        thread.daemon = True
        thread.start()
