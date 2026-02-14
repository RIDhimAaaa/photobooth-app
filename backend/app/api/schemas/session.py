from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SessionCreateResponse(BaseModel):
    session_id: UUID
    expires_at: datetime
