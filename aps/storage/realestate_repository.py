from dataclasses import dataclass

from .database import Database


@dataclass(frozen=True)
class PropertyRecord:
    id: int
    name: str
    property_type: str
    area_sqm: float
    location: str
    monthly_revenue: float


class RealEstateRepository:
    def __init__(self, database: Database):
        self.database = database

    def ensure_schema(self) -> None:
        with self.database.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS realestate_properties (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    property_type TEXT NOT NULL,
                    area_sqm REAL NOT NULL,
                    location TEXT NOT NULL,
                    monthly_revenue REAL NOT NULL DEFAULT 0,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

    def create_property(self, name: str, property_type: str, area_sqm: float, location: str, monthly_revenue: float = 0) -> PropertyRecord:
        if not name:
            raise ValueError("Property name is required")
        if not property_type:
            raise ValueError("Property type is required")
        if area_sqm < 0:
            raise ValueError("Area cannot be negative")
        if monthly_revenue < 0:
            raise ValueError("Monthly revenue cannot be negative")
        self.ensure_schema()
        with self.database.connect() as connection:
            cursor = connection.execute(
                """
                INSERT INTO realestate_properties (name, property_type, area_sqm, location, monthly_revenue)
                VALUES (?, ?, ?, ?, ?)
                """,
                (name, property_type, area_sqm, location, monthly_revenue),
            )
            return PropertyRecord(
                id=int(cursor.lastrowid),
                name=name,
                property_type=property_type,
                area_sqm=area_sqm,
                location=location,
                monthly_revenue=monthly_revenue,
            )

    def list_properties(self) -> list[PropertyRecord]:
        self.ensure_schema()
        with self.database.connect() as connection:
            rows = connection.execute(
                """
                SELECT id, name, property_type, area_sqm, location, monthly_revenue
                FROM realestate_properties
                ORDER BY id
                """
            ).fetchall()
            return [
                PropertyRecord(
                    id=row["id"],
                    name=row["name"],
                    property_type=row["property_type"],
                    area_sqm=float(row["area_sqm"]),
                    location=row["location"],
                    monthly_revenue=float(row["monthly_revenue"]),
                )
                for row in rows
            ]

    def portfolio_summary(self) -> dict[str, float]:
        self.ensure_schema()
        with self.database.connect() as connection:
            row = connection.execute(
                "SELECT COUNT(*) AS property_count, COALESCE(SUM(monthly_revenue), 0) AS monthly_revenue FROM realestate_properties"
            ).fetchone()
            monthly = float(row["monthly_revenue"])
            return {
                "property_count": int(row["property_count"]),
                "monthly_revenue": monthly,
                "annualized_revenue": monthly * 12,
            }
