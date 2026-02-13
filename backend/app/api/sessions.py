from fastapi import APIRouter

from app.services.session_service import SessionService
from app.store.session_store import SessionStore

router = APIRouter(prefix="/sessions", tags=["sessions"])

_store = SessionStore()
_service = SessionService(_store)


@router.post("/")
def create_session():
    session = _service.create_session()
    return {
        "session_id": str(session.id),
        "expires_at": session.expires_at.isoformat(),
    }
