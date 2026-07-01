from dataclasses import dataclass, field

from .module import ModuleDescriptor


@dataclass
class ModuleRegistry:
    _modules: dict[str, ModuleDescriptor] = field(default_factory=dict)

    def register(self, descriptor: ModuleDescriptor) -> None:
        if descriptor.name in self._modules:
            raise ValueError(f"Module already registered: {descriptor.name}")
        self._modules[descriptor.name] = descriptor

    def get(self, name: str) -> ModuleDescriptor:
        try:
            return self._modules[name]
        except KeyError as exc:
            raise KeyError(f"Unknown module: {name}") from exc

    def all(self) -> list[ModuleDescriptor]:
        return list(self._modules.values())

    def names(self) -> set[str]:
        return set(self._modules)
