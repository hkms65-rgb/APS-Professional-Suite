import json, sqlite3
from typing import Any

class SQLiteStore:
    def __init__(self, path=':memory:'):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.execute('CREATE TABLE IF NOT EXISTS records(collection TEXT, key TEXT, payload TEXT, PRIMARY KEY(collection,key))')
        self.conn.commit()

    def put(self, collection: str, key: str, payload: dict[str, Any]) -> None:
        self.conn.execute('INSERT OR REPLACE INTO records VALUES(?,?,?)', (collection, key, json.dumps(payload)))
        self.conn.commit()

    def list(self, collection: str) -> list[dict[str, Any]]:
        rows = self.conn.execute('SELECT payload FROM records WHERE collection=?', (collection,)).fetchall()
        return [json.loads(r[0]) for r in rows]
