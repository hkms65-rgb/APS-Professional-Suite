class CRMService:
    def __init__(self): self.accounts=[]
    def create_account(self,name,segment='general'):
        a={'name':name,'segment':segment}; self.accounts.append(a); return a
    def list_accounts(self): return list(self.accounts)
