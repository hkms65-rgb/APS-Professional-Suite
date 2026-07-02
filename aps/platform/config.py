from dataclasses import dataclass
@dataclass(frozen=True)
class RuntimeConfig:
    app_name: str='APS Professional Suite'
    version: str='0.3.0'
