from aps.storage import Database, DatabaseConfig
from aps.storage.work_order_repository import WorkOrderRepository


def test_work_order_repository_round_trip(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / "aps.sqlite3")))
    database.initialize()
    repository = WorkOrderRepository(database)

    created = repository.create_order("A", 1)
    records = repository.list_orders()

    assert created.status == "planned"
    assert len(records) == 1
    assert records[0].item == "A"
