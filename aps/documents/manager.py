class DocumentManager:
    def __init__(self): self.docs=[]
    def create(self,name,content): d={'name':name,'content':content}; self.docs.append(d); return d
