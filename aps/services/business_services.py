class FinanceService:
    def __init__(self): self.budgets={}
    def create_budget(self,name,amount): self.budgets[name]=amount; return {'name':name,'amount':amount}
    def total_budget(self): return sum(self.budgets.values())
class HRService:
    def __init__(self): self.employees=[]
    def add_employee(self,full_name,role): e={'full_name':full_name,'role':role}; self.employees.append(e); return e
    def headcount(self): return len(self.employees)
class WarehouseService:
    def __init__(self): self.items={}
    def receive_item(self,sku,qty): self.items[sku]=self.items.get(sku,0)+qty; return {'sku':sku,'qty':self.items[sku]}
    def inventory_total(self): return sum(self.items.values())
class ManufacturingService:
    def __init__(self): self.orders=[]
    def create_order(self,product,quantity): o={'product':product,'quantity':quantity,'status':'planned'}; self.orders.append(o); return o
class ProcurementService:
    def __init__(self): self.rfqs=[]
    def create_rfq(self,title,category): r={'title':title,'category':category,'status':'open'}; self.rfqs.append(r); return r
class AIStudioService:
    def __init__(self): self.agents=[]
    def create_agent(self,name,purpose): a={'name':name,'purpose':purpose,'status':'draft'}; self.agents.append(a); return a
