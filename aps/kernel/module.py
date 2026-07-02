from dataclasses import dataclass, field
from enum import Enum

class ModuleState(str, Enum):
    PLANNED='planned'
    READY='ready'
    ACTIVE='active'
    COMPLETE='complete'

class ModuleCategory(str, Enum):
    FOUNDATION='foundation'
    INTELLIGENCE='intelligence'
    BUSINESS='business'
    INDUSTRY='industry'
    STUDIO='studio'
    ADMINISTRATION='administration'

@dataclass(frozen=True)
class ModuleDescriptor:
    id: str
    name: str
    category: ModuleCategory
    version: str = '0.2.0'
    state: ModuleState = ModuleState.PLANNED
    dependencies: tuple[str, ...] = field(default_factory=tuple)
    summary: str = ''
