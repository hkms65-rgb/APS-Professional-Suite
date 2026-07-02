from aps.storage import Database, DatabaseConfig
from aps.storage.procurement_repository import ProcurementRepository


def test_procurement_repository_round_trip(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / "aps.sqlite3")))
    database.initialize()
    repository = ProcurementRepository(database)

    created = repository.create_rfq("Supply A", "Category A")
    records = repository.list_rfqs()

    assert created.title == "Supply A"
    assert len(records) == 1
    assert records[0].status == "open"
