from aps.services import RealEstateService
from aps.storage import Database, DatabaseConfig
from aps.storage.realestate_repository import RealEstateRepository


def test_realestate_service_repository_summary(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / "aps.sqlite3")))
    database.initialize()

    service = RealEstateService(RealEstateRepository(database))
    service.create_property("A", "B", 1, "C", 10)

    assert service.portfolio_summary()["property_count"] == 1
