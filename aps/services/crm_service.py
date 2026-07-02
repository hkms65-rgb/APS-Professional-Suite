class CRMService:
    def __init__(self, repository=None):
        self.repository = repository
        self.accounts = []

    def create_account(self, name, segment='general'):
        if not name:
            raise ValueError('Account name is required')
        if self.repository is not None:
            account = self.repository.create_account(name, segment)
            return {'id': account.id, 'name': account.name, 'segment': account.segment}
        account = {'name': name, 'segment': segment}
        self.accounts.append(account)
        return account

    def list_accounts(self):
        if self.repository is not None:
            return [
                {'id': account.id, 'name': account.name, 'segment': account.segment}
                for account in self.repository.list_accounts()
            ]
        return list(self.accounts)
