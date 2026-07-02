from dataclasses import dataclass

from .database import Database


@dataclass(frozen=True)
class EmployeeRecord:
    id: int
    full_name: str
    role: str


class HRRepository:
    def __init__(self, database: Database):
        self.database = database

    def ensure_schema(self) -> None:
        with self.database.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS hr_employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    role TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

    def add_employee(self, full_name: str, role: str) -> EmployeeRecord:
        if not full_name:
            raise ValueError("Employee full name is required")
        if not role:
            raise ValueError("Employee role is required")
        self.ensure_schema()
        with self.database.connect() as connection:
            cursor = connection.execute(
                "INSERT INTO hr_employees (full_name, role) VALUES (?, ?)",
                (full_name, role),
            )
            return EmployeeRecord(id=int(cursor.lastrowid), full_name=full_name, role=role)

    def headcount(self) -> int:
        self.ensure_schema()
        with self.database.connect() as connection:
            row = connection.execute("SELECT COUNT(*) AS total FROM hr_employees").fetchone()
            return int(row["total"])
