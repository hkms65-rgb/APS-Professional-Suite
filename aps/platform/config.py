from dataclasses import dataclass


@dataclass(frozen=True)
class RuntimeConfig:
    environment: str = "development"
    debug: bool = True
    app_name: str = "APS Professional Suite"
