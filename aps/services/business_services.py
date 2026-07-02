class FinanceService:
    def __init__(self, repository=None):
        self.repository = repository
        self.budgets = {}

    def create_budget(self, name, amount):
        if amount < 0:
            raise ValueError('Budget amount cannot be negative')
        if self.repository is not None:
            budget = self.repository.create_budget(name, amount)
            return {'id': budget.id, 'name': budget.name, 'amount': budget.amount}
        self.budgets[name] = amount
        return {'name': name, 'amount': amount}

    def total_budget(self):
        if self.repository is not None:
            return self.repository.total_budget()
        return sum(self.budgets.values())


class HRService:
    def __init__(self):
        self.employees = []

    def add_employee(self, full_name, role):
        employee = {'full_name': full_name, 'role': role}
        self.employees.append(employee)
        return employee

    def headcount(self):
        return len(self.employees)


class WarehouseService:
    def __init__(self):
        self.items = {}

    def receive_item(self, sku, qty):
        self.items[sku] = self.items.get(sku, 0) + qty
        return {'sku': sku, 'qty': self.items[sku]}

    def inventory_total(self):
        return sum(self.items.values())


class ManufacturingService:
    def __init__(self):
        self.orders = []

    def create_order(self, product, quantity):
        order = {'product': product, 'quantity': quantity, 'status': 'planned'}
        self.orders.append(order)
        return order


class ProcurementService:
    def __init__(self):
        self.rfqs = []

    def create_rfq(self, title, category):
        rfq = {'title': title, 'category': category, 'status': 'open'}
        self.rfqs.append(rfq)
        return rfq


class AIStudioService:
    def __init__(self):
        self.agents = []

    def create_agent(self, name, purpose):
        agent = {'name': name, 'purpose': purpose, 'status': 'draft'}
        self.agents.append(agent)
        return agent
