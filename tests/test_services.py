from aps.services import RealEstateService, CRMService, IdentityService
from aps.domain.realestate import PropertyType

def test_realestate_summary():
    s=RealEstateService()
    s.create_property('Ahmadi Warehouse', PropertyType.WAREHOUSE, 5000, 'Ahmadi', 10000)
    assert s.portfolio_summary()['annualized_revenue'] == 120000

def test_crm_account():
    c=CRMService()
    c.create_account('Client A','industrial')
    assert len(c.list_accounts()) == 1

def test_identity():
    i=IdentityService()
    i.create_role('admin', {'*'})
    assert i.create_user('a@b.com','Admin','admin').can('x')
