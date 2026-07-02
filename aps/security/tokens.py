import base64
import hashlib
import hmac
import json
import time
from dataclasses import dataclass
from typing import Any


class TokenError(ValueError):
    pass


@dataclass(frozen=True)
class TokenService:
    secret: str
    issuer: str = "aps"
    default_ttl_seconds: int = 3600

    def issue(self, subject: str, claims: dict[str, Any] | None = None, ttl_seconds: int | None = None) -> str:
        now = int(time.time())
        payload = {
            "iss": self.issuer,
            "sub": subject,
            "iat": now,
            "exp": now + (ttl_seconds or self.default_ttl_seconds),
            "claims": claims or {},
        }
        payload_bytes = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")
        payload_part = self._encode(payload_bytes)
        signature = self._sign(payload_part)
        return f"{payload_part}.{signature}"

    def verify(self, token: str) -> dict[str, Any]:
        try:
            payload_part, signature = token.split(".", 1)
        except ValueError as exc:
            raise TokenError("Invalid token format") from exc

        expected_signature = self._sign(payload_part)
        if not hmac.compare_digest(signature, expected_signature):
            raise TokenError("Invalid token signature")

        payload = json.loads(self._decode(payload_part).decode("utf-8"))
        if payload.get("iss") != self.issuer:
            raise TokenError("Invalid token issuer")
        if int(payload.get("exp", 0)) < int(time.time()):
            raise TokenError("Token expired")
        return payload

    def _sign(self, payload_part: str) -> str:
        digest = hmac.new(
            self.secret.encode("utf-8"),
            payload_part.encode("utf-8"),
            hashlib.sha256,
        ).digest()
        return self._encode(digest)

    @staticmethod
    def _encode(raw: bytes) -> str:
        return base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")

    @staticmethod
    def _decode(value: str) -> bytes:
        padding = "=" * (-len(value) % 4)
        return base64.urlsafe_b64decode(value + padding)
