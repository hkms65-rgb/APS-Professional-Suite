import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator


@dataclass(frozen=True)
class DatabaseConfig:
    path: str = "aps.sqlite3"


class Database:
    def __init__(self, config: DatabaseConfig | None = None):
        self.config = config or DatabaseConfig()
        self.path = self.config.path

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        if self.path != ":memory:":
            Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        try:
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def initialize(self) -> list[str]:
        from .migrations import MigrationRunner

        return MigrationRunner(self).apply()
