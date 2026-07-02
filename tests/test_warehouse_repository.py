import pytest

from aps.storage import Database, DatabaseConfig
from aps.storage.warehouse_repository import WarehouseRepository


def test_warehouse_repository_receives_and_totals_inventory(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / "aps.sqlite3")))
    database.initialize()
    repository = WarehouseRepository(database)

    first = repository.receive_item("SKU-001", 10)
    second = repository.receive_item("SKU-001", 5)
    repository.receive_item("SKU-002", 7)

    assert first.quantity == 10
    assert second.quantity == 15
    assert repository.inventory_total() == 22


def test_warehouse_repository_rejects_negative_quantity(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / "aps.sqlite3")))
    database.initialize()
    repository = WarehouseRepository(database)

    with pytest.raises(ValueError):
        repository.receive_item("SKU-001", -1)
