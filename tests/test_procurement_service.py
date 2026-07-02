from aps.services import ProcurementService
from aps.storage import Database, DatabaseConfig
from aps.storage.procurement_repository import ProcurementRepository


def test_procurement_service_uses_repository(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / "aps.sqlite3")))
    database.initialize()

    service = ProcurementService(ProcurementRepository(database))
    service.create_rfq("Item A", "Group A")

    assert service.list_rfqs()[0]["title"] == "Item A"
