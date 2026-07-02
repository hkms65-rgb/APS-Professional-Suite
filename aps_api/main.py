from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from aps.platform import build_default_kernel, RuntimeConfig
from aps.services import (
    FinanceService,
    HRService,
    WarehouseService,
    ManufacturingService,
    ProcurementService,
    AIStudioService,
    RealEstateService,
    CRMService,
)
from aps.storage import CRMRepository, Database, DatabaseConfig, FinanceRepository


config = RuntimeConfig.from_env()
app = FastAPI(title=config.app_name, version=config.version)
app.mount('/static', StaticFiles(directory='web/static'), name='static')
app.mount('/apps', StaticFiles(directory='web/apps', html=True), name='apps')

kernel = build_default_kernel()
kernel.start()

database = Database(DatabaseConfig(path=config.database_path))
database.initialize()

finance = FinanceService(FinanceRepository(database))
hr = HRService()
wh = WarehouseService()
mfg = ManufacturingService()
proc = ProcurementService()
ai = AIStudioService()
re = RealEstateService()
crm = CRMService(CRMRepository(database))


class Budget(BaseModel):
    name: str
    amount: float


class Employee(BaseModel):
    full_name: str
    role: str


class Inventory(BaseModel):
    sku: str
    qty: int


class Account(BaseModel):
    name: str
    segment: str = 'general'


@app.get('/')
def index():
    return RedirectResponse('/static/index.html')


@app.get('/api/health')
def health():
    return {
        'status': 'ok',
        'version': config.version,
        'environment': config.environment,
        'kernel': kernel.status.value,
    }


@app.get('/api/modules')
def modules():
    return [{'id': m.id, 'name': m.name, 'state': m.state.value, 'summary': m.summary} for m in kernel.registry.all()]


@app.post('/api/finance/budgets')
def budget(b: Budget):
    return finance.create_budget(b.name, b.amount)


@app.get('/api/finance/summary')
def finance_summary():
    return {'total_budget': finance.total_budget()}


@app.post('/api/hr/employees')
def employee(e: Employee):
    return hr.add_employee(e.full_name, e.role)


@app.get('/api/hr/summary')
def hr_summary():
    return {'headcount': hr.headcount()}


@app.post('/api/warehouse/receive')
def receive(i: Inventory):
    return wh.receive_item(i.sku, i.qty)


@app.get('/api/warehouse/summary')
def wh_summary():
    return {'inventory_total': wh.inventory_total()}


@app.post('/api/crm/accounts')
def account(a: Account):
    return crm.create_account(a.name, a.segment)


@app.get('/api/crm/accounts')
def accounts():
    return crm.list_accounts()


@app.get('/api/realestate/summary')
def re_summary():
    return re.portfolio_summary()
