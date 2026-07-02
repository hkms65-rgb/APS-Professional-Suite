from dataclasses import dataclass

from .database import Database


@dataclass(frozen=True)
class InventoryRecord:
    sku: str
    quantity: int


class WarehouseRepository:
    def __init__(self, database: Database):
        self.database = database

    def ensure_schema(self) -> None:
        with self.database.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS warehouse_inventory (
                    sku TEXT PRIMARY KEY,
                    quantity INTEGER NOT NULL DEFAULT 0,
                    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

    def receive_item(self, sku: str, quantity: int) -> InventoryRecord:
        if quantity < 0:
            raise ValueError("Received quantity cannot be negative")
        self.ensure_schema()
        with self.database.connect() as connection:
            row = connection.execute(
                "SELECT quantity FROM warehouse_inventory WHERE sku = ?",
                (sku,),
            ).fetchone()
            current = int(row["quantity"]) if row else 0
            new_quantity = current + quantity
            connection.execute(
                """
                INSERT INTO warehouse_inventory (sku, quantity, updated_at)
                VALUES (?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(sku) DO UPDATE SET
                    quantity = excluded.quantity,
                    updated_at = CURRENT_TIMESTAMP
                """,
                (sku, new_quantity),
            )
            return InventoryRecord(sku=sku, quantity=new_quantity)

    def inventory_total(self) -> int:
        self.ensure_schema()
        with self.database.connect() as connection:
            row = connection.execute(
                "SELECT COALESCE(SUM(quantity), 0) AS total FROM warehouse_inventory"
            ).fetchone()
            return int(row["total"])
