from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(frozen=True)
class Role:
    name: str
    permissions: frozenset[str]
    role_id: str = field(default_factory=lambda: str(uuid4()))

    def allows(self, permission: str) -> bool:
        return "*" in self.permissions or permission in self.permissions


@dataclass(frozen=True)
class User:
    email: str
    full_name: str
    role: Role
    user_id: str = field(default_factory=lambda: str(uuid4()))
    is_active: bool = True
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def can(self, permission: str) -> bool:
        return self.is_active and self.role.allows(permission)
