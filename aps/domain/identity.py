from dataclasses import dataclass, field

@dataclass
class Role:
    name: str
    permissions: set[str] = field(default_factory=set)

    def allows(self, permission: str) -> bool:
        return permission in self.permissions or '*' in self.permissions

@dataclass
class User:
    email: str
    full_name: str
    role: Role

    def can(self, permission: str) -> bool:
        return self.role.allows(permission)
