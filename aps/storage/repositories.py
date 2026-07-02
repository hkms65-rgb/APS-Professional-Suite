from dataclasses import dataclass

from .database import Database


@dataclass(frozen=True)
class CRMAccountRecord:
    id: int
    name: str
    segment: str


@dataclass(frozen=True)
class BudgetRecord:
    id: int
    name: str
    amount: float


class CRMRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_account(self, name: str, segment: str = "general") -> CRMAccountRecord:
        with self.database.connect() as connection:
            cursor = connection.execute(
                "INSERT INTO crm_accounts (name, segment) VALUES (?, ?)",
                (name, segment),
            )
            account_id = int(cursor.lastrowid)
            return CRMAccountRecord(id=account_id, name=name, segment=segment)

    def list_accounts(self) -> list[CRMAccountRecord]:
        with self.database.connect() as connection:
            rows = connection.execute(
                "SELECT id, name, segment FROM crm_accounts ORDER BY id"
            ).fetchall()
            return [CRMAccountRecord(id=row["id"], name=row["name"], segment=row["segment"]) for row in rows]


class FinanceRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_budget(self, name: str, amount: float) -> BudgetRecord:
        with self.database.connect() as connection:
            cursor = connection.execute(
                "INSERT INTO finance_budgets (name, amount) VALUES (?, ?)",
                (name, amount),
            )
            budget_id = int(cursor.lastrowid)
            return BudgetRecord(id=budget_id, name=name, amount=amount)

    def total_budget(self) -> float:
        with self.database.connect() as connection:
            row = connection.execute("SELECT COALESCE(SUM(amount), 0) AS total FROM finance_budgets").fetchone()
            return float(row["total"])
