from dataclasses import dataclass
from typing import Iterable

from .database import Database


@dataclass(frozen=True)
class Migration:
    version: str
    description: str
    sql: str


MIGRATIONS: tuple[Migration, ...] = (
    Migration(
        version="0001",
        description="Create CRM and finance tables",
        sql="""
        CREATE TABLE IF NOT EXISTS crm_accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            segment TEXT NOT NULL DEFAULT 'general',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS finance_budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            amount REAL NOT NULL CHECK(amount >= 0),
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        """,
    ),
)


class MigrationRunner:
    def __init__(self, database: Database, migrations: Iterable[Migration] = MIGRATIONS):
        self.database = database
        self.migrations = tuple(migrations)

    def apply(self) -> list[str]:
        applied: list[str] = []
        with self.database.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS schema_migrations (
                    version TEXT PRIMARY KEY,
                    description TEXT NOT NULL,
                    applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            existing = {
                row["version"]
                for row in connection.execute("SELECT version FROM schema_migrations").fetchall()
            }
            for migration in self.migrations:
                if migration.version in existing:
                    continue
                connection.executescript(migration.sql)
                connection.execute(
                    "INSERT INTO schema_migrations (version, description) VALUES (?, ?)",
                    (migration.version, migration.description),
                )
                applied.append(migration.version)
        return applied
