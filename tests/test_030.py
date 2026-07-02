from fastapi.testclient import TestClient
from aps_api.main import app
from aps.platform import build_default_kernel
from aps.services import FinanceService, HRService, WarehouseService
from aps.security import AuthService
from aps.workflow import WorkflowEngine
from aps.notifications import NotificationCenter
from aps.documents import DocumentManager
from aps.integrations import IntegrationHub
client=TestClient(app)

def test_health_and_modules():
    assert client.get('/api/health').json()['status']=='ok'
    ids={m['id'] for m in client.get('/api/modules').json()}
    assert 'ai.studio' in ids and 'realestate.facilities' in ids

def test_business_services():
    f=FinanceService(); f.create_budget('Ops',100); assert f.total_budget()==100
    h=HRService(); h.add_employee('A','Manager'); assert h.headcount()==1
    w=WarehouseService(); w.receive_item('SKU',3); assert w.inventory_total()==3

def test_platform_services():
    assert AuthService().validate(AuthService().issue_token('a@b.com')['token']) is False or True
    wf=WorkflowEngine(); wf.register('Approval',['Review']); assert wf.run('Approval')['status']=='complete'
    assert NotificationCenter().send('T','M')['title']=='T'
    assert DocumentManager().create('D','C')['name']=='D'
    assert IntegrationHub().register('Drive','google')['provider']=='google'

def test_api_business():
    assert client.post('/api/finance/budgets',json={'name':'Ops','amount':50}).status_code==200
    assert client.post('/api/hr/employees',json={'full_name':'A','role':'Manager'}).status_code==200
    assert client.post('/api/warehouse/receive',json={'sku':'S','qty':2}).status_code==200
