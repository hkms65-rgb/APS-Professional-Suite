from dataclasses import dataclass

@dataclass(frozen=True)
class RuntimeConfig:
    environment: str = 'development'
    app_name: str = 'APS Professional Suite'
    version: str = '0.2.0'
