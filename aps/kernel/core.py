from dataclasses import dataclass, field
from enum import Enum
from .registry import ModuleRegistry
from .module import ModuleDescriptor

class KernelStatus(str, Enum):
    CREATED='created'
    BOOTSTRAPPED='bootstrapped'
    RUNNING='running'

@dataclass
class Kernel:
    status: KernelStatus = KernelStatus.CREATED
    registry: ModuleRegistry = field(default_factory=ModuleRegistry)

    def bootstrap(self) -> None:
        self.status = KernelStatus.BOOTSTRAPPED

    def start(self) -> None:
        if self.status == KernelStatus.CREATED:
            self.bootstrap()
        self.status = KernelStatus.RUNNING

    def register_module(self, descriptor: ModuleDescriptor) -> None:
        self.registry.register(descriptor)
