from dataclasses import dataclass

from .database import Database


@dataclass(frozen=True)
class WorkOrderRecord:
    id: int
    item: str
    quantity: int
    status: str


class WorkOrderRepository:
    def __init__(self, database: Database):
        self.database = database

    def ensure_schema(self) -> None:
        with self.database.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS work_orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    status TEXT NOT NULL DEFAULT 'planned',
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

    def create_order(self, item: str, quantity: int) -> WorkOrderRecord:
        if not item:
            raise ValueError("Item is required")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.ensure_schema()
        with self.database.connect() as connection:
            cursor = connection.execute(
                "INSERT INTO work_orders (item, quantity, status) VALUES (?, ?, ?)",
                (item, quantity, "planned"),
            )
            return WorkOrderRecord(id=int(cursor.lastrowid), item=item, quantity=quantity, status="planned")

    def list_orders(self) -> list[WorkOrderRecord]:
        self.ensure_schema()
        with self.database.connect() as connection:
            rows = connection.execute("SELECT id, item, quantity, status FROM work_orders ORDER BY id").fetchall()
            return [
                WorkOrderRecord(id=row["id"], item=row["item"], quantity=row["quantity"], status=row["status"])
                for row in rows
            ]
