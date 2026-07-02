import pytest

from aps.services import RealEstateService, CRMService, IdentityService, FinanceService
from aps.domain.realestate import PropertyType
from aps.storage import CRMRepository, Database, DatabaseConfig, FinanceRepository


def test_realestate_summary():
    s=RealEstateService()
    s.create_property('Ahmadi Warehouse', PropertyType.WAREHOUSE, 5000, 'Ahmadi', 10000)
    assert s.portfolio_summary()['annualized_revenue'] == 120000


def test_crm_account():
    c=CRMService()
    c.create_account('Client A','industrial')
    assert len(c.list_accounts()) == 1


def test_finance_budget():
    f = FinanceService()
    f.create_budget('Operations', 1000)
    assert f.total_budget() == 1000


def test_identity():
    i=IdentityService()
    i.create_role('admin', {'*'})
    assert i.create_user('a@b.com','Admin','admin').can('x')


def test_identity_authentication_success_and_failure():
    i = IdentityService()
    i.create_role('operator', {'warehouse.receive'})
    user = i.create_user('operator@example.com', 'Warehouse Operator', 'operator', password='valid-passphrase')

    assert i.authenticate('operator@example.com', 'valid-passphrase') == user
    assert i.authenticate('operator@example.com', 'invalid-passphrase') is None
    assert i.authenticate('missing@example.com', 'valid-passphrase') is None


def test_identity_permission_enforcement():
    i = IdentityService()
    i.create_role('finance', {'finance.read'})
    user = i.create_user('finance@example.com', 'Finance User', 'finance', password='finance-passphrase')

    i.require_permission(user, 'finance.read')
    with pytest.raises(PermissionError):
        i.require_permission(user, 'warehouse.receive')


def test_identity_rejects_unknown_role_and_duplicate_user():
    i = IdentityService()
    with pytest.raises(KeyError):
        i.create_user('nobody@example.com', 'No Role', 'missing-role')

    i.create_role('admin', {'*'})
    i.create_user('admin@example.com', 'Admin', 'admin', password='admin-passphrase')
    with pytest.raises(ValueError):
        i.create_user('admin@example.com', 'Admin Again', 'admin', password='admin-passphrase')


def test_crm_service_uses_repository_when_provided(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / 'aps.sqlite3')))
    database.initialize()

    service = CRMService(CRMRepository(database))
    service.create_account('Persistent Client', 'enterprise')

    reloaded = CRMService(CRMRepository(Database(DatabaseConfig(path=str(tmp_path / 'aps.sqlite3')))))
    assert reloaded.list_accounts() == [{'id': 1, 'name': 'Persistent Client', 'segment': 'enterprise'}]


def test_finance_service_uses_repository_when_provided(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / 'aps.sqlite3')))
    database.initialize()

    service = FinanceService(FinanceRepository(database))
    service.create_budget('Operations', 1000)
    service.create_budget('Facilities', 500)

    reloaded = FinanceService(FinanceRepository(Database(DatabaseConfig(path=str(tmp_path / 'aps.sqlite3')))))
    assert reloaded.total_budget() == 1500
