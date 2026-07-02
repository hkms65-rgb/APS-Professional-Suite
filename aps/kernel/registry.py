from dataclasses import dataclass, field
from .module import ModuleDescriptor
@dataclass
class ModuleRegistry:
    _modules: dict[str, ModuleDescriptor]=field(default_factory=dict)
    def register(self, descriptor: ModuleDescriptor): self._modules[descriptor.id]=descriptor
    def get(self, module_id: str): return self._modules[module_id]
    def all(self): return list(self._modules.values())
