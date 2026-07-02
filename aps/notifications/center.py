class NotificationCenter:
    def __init__(self): self.items=[]
    def send(self,title,message): n={'title':title,'message':message}; self.items.append(n); return n
