import hashlib
import hmac
import secrets
from dataclasses import dataclass

from aps.domain.identity import Role, User


@dataclass(frozen=True)
class StoredCredential:
    user: User
    salt: str
    password_hash: str


class IdentityService:
    def __init__(self):
        self.roles: dict[str, Role] = {}
        self._credentials: dict[str, StoredCredential] = {}

    def create_role(self, name: str, permissions: set[str] | frozenset[str]) -> Role:
        role = Role(name=name, permissions=frozenset(permissions))
        self.roles[name] = role
        return role

    def create_user(
        self,
        email: str,
        full_name: str,
        role_name: str,
        password: str | None = None,
    ) -> User:
        if role_name not in self.roles:
            raise KeyError(f"Unknown role: {role_name}")
        if email in self._credentials:
            raise ValueError(f"User already exists: {email}")

        user = User(email=email, full_name=full_name, role=self.roles[role_name])
        salt = secrets.token_hex(16)
        password_hash = self._hash_password(password or secrets.token_urlsafe(24), salt)
        self._credentials[email] = StoredCredential(user=user, salt=salt, password_hash=password_hash)
        return user

    def authenticate(self, email: str, password: str) -> User | None:
        credential = self._credentials.get(email)
        if credential is None:
            return None
        candidate = self._hash_password(password, credential.salt)
        if hmac.compare_digest(candidate, credential.password_hash):
            return credential.user
        return None

    def require_permission(self, user: User, permission: str) -> None:
        if not user.can(permission):
            raise PermissionError(f"Permission denied: {permission}")

    @staticmethod
    def _hash_password(password: str, salt: str) -> str:
        return hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt.encode("utf-8"),
            120_000,
        ).hex()
