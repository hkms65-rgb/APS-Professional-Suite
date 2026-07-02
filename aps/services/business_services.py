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
    def __init__(self, repository=None):
        self.repository = repository
        self.employees = []

    def add_employee(self, full_name, role):
        if self.repository is not None:
            employee = self.repository.add_employee(full_name, role)
            return {'id': employee.id, 'full_name': employee.full_name, 'role': employee.role}
        employee = {'full_name': full_name, 'role': role}
        self.employees.append(employee)
        return employee

    def headcount(self):
        if self.repository is not None:
            return self.repository.headcount()
        return len(self.employees)


class WarehouseService:
    def __init__(self, repository=None):
        self.repository = repository
        self.items = {}

    def receive_item(self, sku, qty):
        if qty < 0:
            raise ValueError('Received quantity cannot be negative')
        if self.repository is not None:
            item = self.repository.receive_item(sku, qty)
            return {'sku': item.sku, 'qty': item.quantity}
        self.items[sku] = self.items.get(sku, 0) + qty
        return {'sku': sku, 'qty': self.items[sku]}

    def inventory_total(self):
        if self.repository is not None:
            return self.repository.inventory_total()
        return sum(self.items.values())


class ManufacturingService:
    def __init__(self, repository=None):
        self.repository = repository
        self.orders = []

    def create_order(self, product, quantity):
        if self.repository is not None:
            record = self.repository.create_order(str(product), quantity)
            return {'id': record.id, 'product': record.item, 'quantity': record.quantity, 'status': record.status}
        order = {'product': product, 'quantity': quantity, 'status': 'planned'}
        self.orders.append(order)
        return order

    def list_orders(self):
        if self.repository is not None:
            return [
                {'id': record.id, 'product': record.item, 'quantity': record.quantity, 'status': record.status}
                for record in self.repository.list_orders()
            ]
        return list(self.orders)


class ProcurementService:
    def __init__(self, repository=None):
        self.repository = repository
        self.rfqs = []

    def create_rfq(self, title, category):
        if self.repository is not None:
            record = self.repository.create_rfq(title, category)
            return {'id': record.id, 'title': record.title, 'category': record.category, 'status': record.status}
        rfq = {'title': title, 'category': category, 'status': 'open'}
        self.rfqs.append(rfq)
        return rfq

    def list_rfqs(self):
        if self.repository is not None:
            return [
                {'id': record.id, 'title': record.title, 'category': record.category, 'status': record.status}
                for record in self.repository.list_rfqs()
            ]
        return list(self.rfqs)


class AIStudioService:
    def __init__(self):
        self.agents = []

    def create_agent(self, name, purpose):
        agent = {'name': name, 'purpose': purpose, 'status': 'draft'}
        self.agents.append(agent)
        return agent
