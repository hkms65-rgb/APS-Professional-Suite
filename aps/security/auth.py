from .tokens import TokenError, TokenService


class AuthService:
    def __init__(self, token_service: TokenService | None = None):
        self.token_service = token_service or TokenService(secret="development-secret-change-me")

    def issue_token(self, user_email):
        token = self.token_service.issue(user_email)
        return {"token": token, "user_email": user_email}

    def validate(self, token):
        try:
            self.token_service.verify(token)
            return True
        except TokenError:
            return False

    def subject(self, token):
        payload = self.token_service.verify(token)
        return payload["sub"]
