from aps.storage import Database, DatabaseConfig
from aps.storage.hr_repository import HRRepository


def test_hr_repository_round_trip(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / "aps.sqlite3")))
    database.initialize()
    repository = HRRepository(database)

    repository.add_employee("A", "B")

    assert repository.headcount() == 1
