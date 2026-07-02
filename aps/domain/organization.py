from dataclasses import dataclass, field

@dataclass
class Organization:
    name: str
    units: list[str] = field(default_factory=list)

    def add_unit(self, name: str) -> None:
        self.units.append(name)
