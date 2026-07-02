from aps.security import AuthService, TokenService


def test_auth_service_issues_valid_signed_token():
    auth = AuthService(TokenService(secret="test-secret"))

    issued = auth.issue_token("user@example.com")

    assert issued["user_email"] == "user@example.com"
    assert auth.validate(issued["token"])
    assert auth.subject(issued["token"]) == "user@example.com"


def test_auth_service_rejects_invalid_token():
    auth = AuthService(TokenService(secret="test-secret"))

    assert not auth.validate("invalid-token")
