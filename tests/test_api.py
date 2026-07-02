from fastapi.testclient import TestClient

from aps_api.main import app

client = TestClient(app)


def test_health():
    assert client.get('/api/health').json()['status'] == 'ok'


def test_modules_api():
    ids = {m['id'] for m in client.get('/api/modules').json()}
    assert 'crm' in ids
    assert 'realestate.facilities' in ids


def test_crm_api():
    response = client.post('/api/crm/accounts', json={'name': 'Client B', 'segment': 'logistics'})
    assert response.status_code == 200
    assert response.json()['name'] == 'Client B'

    accounts = client.get('/api/crm/accounts')
    assert accounts.status_code == 200
    assert any(account['name'] == 'Client B' for account in accounts.json())


def test_finance_api():
    response = client.post('/api/finance/budgets', json={'name': 'Budget B', 'amount': 1200})
    assert response.status_code == 200

    summary = client.get('/api/finance/summary')
    assert summary.status_code == 200
    assert summary.json()['total_budget'] >= 1200
