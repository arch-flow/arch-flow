import uuid
from typing import Optional
from sqlalchemy.types import TypeDecorator, String

class GUID(TypeDecorator):
    impl = String(36)
    cache_ok = True

    def process_bind_param(self, value: Optional[uuid.UUID], dialect):
        if value is None:
            return None
        if isinstance(value, uuid.UUID):
            return str(value)
        return str(uuid.UUID(str(value)))

    def process_result_value(self, value: Optional[str], dialect):
        if value is None:
            return None
        return uuid.UUID(value)

