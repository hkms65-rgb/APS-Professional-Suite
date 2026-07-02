from dataclasses import asdict
from aps.domain.crm import Account
from aps.persistence import SQLiteStore

class CRMService:
    def __init__(self, store=None):
        self.store = store or SQLiteStore()

    def create_account(self, name: str, segment: str='general') -> Account:
        account = Account(name=name, segment=segment)
        self.store.put('accounts', account.account_id, asdict(account))
        return account

    def list_accounts(self):
        return self.store.list('accounts')
