from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from aps.platform import build_default_kernel, RuntimeConfig
from aps.services import RealEstateService, CRMService
from aps.domain.realestate import PropertyType

app = FastAPI(title='APS Professional Suite', version='0.2.0')
app.mount('/static', StaticFiles(directory='web/static'), name='static')
app.mount('/apps', StaticFiles(directory='web/apps', html=True), name='apps')

config = RuntimeConfig()
kernel = build_default_kernel(); kernel.start()
realestate = RealEstateService()
crm = CRMService()

class PropertyCreate(BaseModel):
    name: str
    property_type: PropertyType
    area_sqm: float
    location: str
    monthly_revenue: float = 0.0

class AccountCreate(BaseModel):
    name: str
    segment: str = 'general'

@app.get('/')
def index():
    return RedirectResponse('/static/index.html')

@app.get('/api/health')
def health():
    return {'status':'ok','version':config.version,'kernel':kernel.status.value}

@app.get('/api/modules')
def modules():
    return [{'id':m.id,'name':m.name,'category':m.category.value,'state':m.state.value,'summary':m.summary} for m in kernel.registry.all()]

@app.post('/api/realestate/properties')
def create_property(payload: PropertyCreate):
    p = realestate.create_property(payload.name, payload.property_type, payload.area_sqm, payload.location, payload.monthly_revenue)
    return {'property_id':p.property_id,'name':p.name}

@app.get('/api/realestate/summary')
def realestate_summary():
    return realestate.portfolio_summary()

@app.post('/api/crm/accounts')
def create_account(payload: AccountCreate):
    a = crm.create_account(payload.name, payload.segment)
    return {'account_id':a.account_id,'name':a.name}

@app.get('/api/crm/accounts')
def accounts():
    return crm.list_accounts()
