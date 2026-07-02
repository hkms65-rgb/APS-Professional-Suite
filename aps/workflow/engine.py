class WorkflowEngine:
    def __init__(self): self.workflows={}
    def register(self,name,steps): self.workflows[name]=steps; return {'name':name,'steps':steps}
    def run(self,name): return {'name':name,'status':'complete','completed_steps':self.workflows[name]}
