from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Callable, Any
from uuid import uuid4


@dataclass(frozen=True)
class DomainEvent:
    name: str
    payload: dict[str, Any]
    event_id: str = field(default_factory=lambda: str(uuid4()))
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class EventBus:
    def __init__(self) -> None:
        self._handlers: dict[str, list[Callable[[DomainEvent], None]]] = {}

    def subscribe(self, event_name: str, handler: Callable[[DomainEvent], None]) -> None:
        self._handlers.setdefault(event_name, []).append(handler)

    def publish(self, event: DomainEvent) -> None:
        for handler in self._handlers.get(event.name, []):
            handler(event)
