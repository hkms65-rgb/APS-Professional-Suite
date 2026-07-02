class IntegrationHub:
    def __init__(self): self.integrations=[]
    def register(self,name,provider): i={'name':name,'provider':provider}; self.integrations.append(i); return i
