from datetime import datetime, timedelta
from uuid import uuid4

from app.models.session import Session
from app.store.session_store import SessionStore


class SessionService:
    SESSION_TTL = timedelta(minutes=30)

    def __init__(self, store: SessionStore) -> None:
        self.store = store

    def create_session(self) -> Session:
        now = datetime.utcnow()
        session = Session(
            id=uuid4(),
            created_at=now,
            expires_at=now + self.SESSION_TTL,
        )
        self.store.save(session)
        return session
