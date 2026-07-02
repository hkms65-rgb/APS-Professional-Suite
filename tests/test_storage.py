from aps.storage import CRMRepository, Database, DatabaseConfig, FinanceRepository


def test_database_initializes_and_persists_crm_accounts(tmp_path):
    db_path = tmp_path / "aps-test.sqlite3"
    database = Database(DatabaseConfig(path=str(db_path)))
    database.initialize()

    writer = CRMRepository(database)
    writer.create_account("Client A", "industrial")

    reader = CRMRepository(Database(DatabaseConfig(path=str(db_path))))
    accounts = reader.list_accounts()

    assert len(accounts) == 1
    assert accounts[0].name == "Client A"
    assert accounts[0].segment == "industrial"


def test_database_initializes_and_persists_finance_budgets(tmp_path):
    db_path = tmp_path / "aps-test.sqlite3"
    database = Database(DatabaseConfig(path=str(db_path)))
    database.initialize()

    writer = FinanceRepository(database)
    writer.create_budget("Operations", 1250.50)
    writer.create_budget("Facilities", 2500)

    reader = FinanceRepository(Database(DatabaseConfig(path=str(db_path))))

    assert reader.total_budget() == 3750.50
