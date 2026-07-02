from fastapi.testclient import TestClient
from aps_api.main import app
client=TestClient(app)

def test_health():
    assert client.get('/api/health').json()['status'] == 'ok'

def test_modules_api():
    ids={m['id'] for m in client.get('/api/modules').json()}
    assert 'crm' in ids
    assert 'realestate.facilities' in ids

def test_crm_api():
    r=client.post('/api/crm/accounts', json={'name':'Client B','segment':'logistics'})
    assert r.status_code == 200
