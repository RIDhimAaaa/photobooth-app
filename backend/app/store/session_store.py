from datetime import datetime
from typing import Dict
from uuid import UUID

from app.models.session import Session


class SessionStore:
    def __init__(self) -> None:
        self._sessions: Dict[UUID, Session] = {}

    def save(self, session: Session) -> None:
        self._sessions[session.id] = session

    def get(self, session_id: UUID) -> Session | None:
        return self._sessions.get(session_id)

    def cleanup_expired(self) -> None:
        now = datetime.utcnow()
        expired_ids = [
            sid for sid, s in self._sessions.items()
            if s.expires_at < now
        ]
        for sid in expired_ids:
            self._sessions.pop(sid)
