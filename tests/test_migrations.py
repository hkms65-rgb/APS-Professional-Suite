from aps.storage import Database, DatabaseConfig


def test_initialize_records_first_migration(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / "aps.sqlite3")))

    applied = database.initialize()

    assert applied == ["0001"]


def test_initialize_runs_only_new_migrations(tmp_path):
    database = Database(DatabaseConfig(path=str(tmp_path / "aps.sqlite3")))

    first = database.initialize()
    second = database.initialize()

    assert first == ["0001"]
    assert second == []
