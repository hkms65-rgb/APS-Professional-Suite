from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable
from uuid import uuid4

@dataclass(frozen=True)
class DomainEvent:
    name: str
    payload: dict[str, Any]
    event_id: str = field(default_factory=lambda: str(uuid4()))
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

class EventBus:
    def __init__(self):
        self._handlers = {}

    def subscribe(self, name: str, handler: Callable[[DomainEvent], None]) -> None:
        self._handlers.setdefault(name, []).append(handler)

    def publish(self, event: DomainEvent) -> None:
        for h in self._handlers.get(event.name, []):
            h(event)
