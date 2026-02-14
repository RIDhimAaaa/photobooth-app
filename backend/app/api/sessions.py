from fastapi import APIRouter

from app.api.schemas.session import SessionCreateResponse
from app.services.session_service import SessionService
from app.store.session_store import SessionStore

router = APIRouter(prefix="/sessions", tags=["sessions"])

_store = SessionStore()
_service = SessionService(_store)


@router.post("/", response_model=SessionCreateResponse)
def create_session():
    session = _service.create_session()
    return SessionCreateResponse(
        session_id=session.id,
        expires_at=session.expires_at,
    )
