from aps.storage import Database, DatabaseConfig
from aps.storage.realestate_repository import RealEstateRepository


def test_realestate_repository_creates_property_and_summary(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / "aps.sqlite3")))
    database.initialize()
    repository = RealEstateRepository(database)

    created = repository.create_property("Property A", "warehouse", 1000, "Location A", 500)
    summary = repository.portfolio_summary()

    assert created.name == "Property A"
    assert summary == {
        "property_count": 1,
        "monthly_revenue": 500.0,
        "annualized_revenue": 6000.0,
    }
