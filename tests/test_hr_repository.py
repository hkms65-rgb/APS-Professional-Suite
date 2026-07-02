import pytest

from aps.storage import Database, DatabaseConfig
from aps.storage.hr_repository import HRRepository


def test_hr_repository_adds_employee_and_counts(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / "aps.sqlite3")))
    database.initialize()
    repository = HRRepository(database)

    employee = repository.add_employee("User A", "Role A")

    assert employee.full_name == "User A"
    assert repository.headcount() == 1


def test_hr_repository_requires_name_and_role(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / "aps.sqlite3")))
    database.initialize()
    repository = HRRepository(database)

    with pytest.raises(ValueError):
        repository.add_employee("", "Role A")

    with pytest.raises(ValueError):
        repository.add_employee("User A", "")
