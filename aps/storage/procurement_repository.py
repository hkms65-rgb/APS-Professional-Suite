from dataclasses import dataclass

from .database import Database


@dataclass(frozen=True)
class RFQRecord:
    id: int
    title: str
    category: str
    status: str


class ProcurementRepository:
    def __init__(self, database: Database):
        self.database = database

    def ensure_schema(self) -> None:
        with self.database.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS procurement_rfqs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    category TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'open',
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

    def create_rfq(self, title: str, category: str) -> RFQRecord:
        if not title:
            raise ValueError("RFQ title is required")
        if not category:
            raise ValueError("RFQ category is required")
        self.ensure_schema()
        with self.database.connect() as connection:
            cursor = connection.execute(
                "INSERT INTO procurement_rfqs (title, category, status) VALUES (?, ?, ?)",
                (title, category, "open"),
            )
            return RFQRecord(id=int(cursor.lastrowid), title=title, category=category, status="open")

    def list_rfqs(self) -> list[RFQRecord]:
        self.ensure_schema()
        with self.database.connect() as connection:
            rows = connection.execute(
                "SELECT id, title, category, status FROM procurement_rfqs ORDER BY id"
            ).fetchall()
            return [
                RFQRecord(id=row["id"], title=row["title"], category=row["category"], status=row["status"])
                for row in rows
            ]
