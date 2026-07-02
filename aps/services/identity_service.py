from aps.domain.identity import Role, User

class IdentityService:
    def __init__(self):
        self.roles = {}

    def create_role(self, name: str, permissions: set[str]) -> Role:
        role = Role(name, permissions)
        self.roles[name] = role
        return role

    def create_user(self, email: str, full_name: str, role_name: str) -> User:
        return User(email, full_name, self.roles[role_name])
