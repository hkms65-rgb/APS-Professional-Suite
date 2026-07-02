import pytest

from aps.security import TokenError, TokenService


def test_token_service_issues_and_verifies_token():
    service = TokenService(secret="test-secret", issuer="aps-test")

    token = service.issue("user@example.com", {"role": "admin"})
    payload = service.verify(token)

    assert payload["sub"] == "user@example.com"
    assert payload["claims"] == {"role": "admin"}
    assert payload["iss"] == "aps-test"


def test_token_service_rejects_tampered_token():
    service = TokenService(secret="test-secret")
    token = service.issue("user@example.com")
    payload, signature = token.split(".", 1)

    with pytest.raises(TokenError):
        service.verify(payload + "x." + signature)


def test_token_service_rejects_expired_token():
    service = TokenService(secret="test-secret")
    token = service.issue("user@example.com", ttl_seconds=-1)

    with pytest.raises(TokenError):
        service.verify(token)
