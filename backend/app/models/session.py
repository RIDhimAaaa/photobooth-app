from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Session:
    id: UUID
    created_at: datetime
    expires_at: datetime
