from dataclasses import dataclass, field
from enum import Enum
from typing import Dict

from .module import ModuleDescriptor
from .registry import ModuleRegistry


class KernelStatus(str, Enum):
    CREATED = "created"
    BOOTSTRAPPED = "bootstrapped"
    RUNNING = "running"
    STOPPED = "stopped"


@dataclass
class Kernel:
    name: str = "APS Enterprise Kernel"
    status: KernelStatus = KernelStatus.CREATED
    registry: ModuleRegistry = field(default_factory=ModuleRegistry)

    def bootstrap(self) -> None:
        if self.status != KernelStatus.CREATED:
            raise RuntimeError("Kernel can only bootstrap from CREATED state.")
        self.status = KernelStatus.BOOTSTRAPPED

    def start(self) -> None:
        if self.status not in {KernelStatus.CREATED, KernelStatus.BOOTSTRAPPED}:
            raise RuntimeError("Kernel cannot start from current state.")
        if self.status == KernelStatus.CREATED:
            self.bootstrap()
        self.status = KernelStatus.RUNNING

    def stop(self) -> None:
        if self.status != KernelStatus.RUNNING:
            raise RuntimeError("Kernel can only stop from RUNNING state.")
        self.status = KernelStatus.STOPPED

    def register_module(self, descriptor: ModuleDescriptor) -> None:
        self.registry.register(descriptor)

    def module_summary(self) -> Dict[str, str]:
        return {module.name: module.state.value for module in self.registry.all()}
