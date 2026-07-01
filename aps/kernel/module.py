from dataclasses import dataclass, field
from enum import Enum


class ModuleState(str, Enum):
    PLANNED = "planned"
    READY = "ready"
    ACTIVE = "active"
    COMPLETE = "complete"


@dataclass(frozen=True)
class ModuleDescriptor:
    name: str
    version: str = "0.0.1"
    state: ModuleState = ModuleState.PLANNED
    dependencies: tuple[str, ...] = field(default_factory=tuple)

    def is_dependency_ready(self, completed_modules: set[str]) -> bool:
        return all(dependency in completed_modules for dependency in self.dependencies)
