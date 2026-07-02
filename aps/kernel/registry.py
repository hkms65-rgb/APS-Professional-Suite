from dataclasses import dataclass, field
from .module import ModuleDescriptor

@dataclass
class ModuleRegistry:
    _modules: dict[str, ModuleDescriptor] = field(default_factory=dict)

    def register(self, descriptor: ModuleDescriptor) -> None:
        if descriptor.id in self._modules:
            raise ValueError(f'Module already registered: {descriptor.id}')
        self._modules[descriptor.id] = descriptor

    def get(self, module_id: str) -> ModuleDescriptor:
        if module_id not in self._modules:
            raise KeyError(module_id)
        return self._modules[module_id]

    def all(self) -> list[ModuleDescriptor]:
        return list(self._modules.values())
