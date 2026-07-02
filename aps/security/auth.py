from uuid import uuid4
class AuthService:
    def __init__(self): self.sessions={}
    def issue_token(self,user_email): 
        token=str(uuid4()); self.sessions[token]=user_email; return {'token':token,'user_email':user_email}
    def validate(self,token): return token in self.sessions
