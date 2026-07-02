import os
from dataclasses import dataclass


@dataclass(frozen=True)
class RuntimeConfig:
    app_name: str = 'APS Professional Suite'
    version: str = '0.3.0'
    environment: str = 'development'
    database_path: str = 'data/aps.sqlite3'
    signing_key: str = 'development-key-change-me'

    @classmethod
    def from_env(cls):
        return cls(
            app_name=os.getenv('APS_APP_NAME', cls.app_name),
            version=os.getenv('APS_VERSION', cls.version),
            environment=os.getenv('APS_ENVIRONMENT', cls.environment),
            database_path=os.getenv('APS_DATABASE_PATH', cls.database_path),
            signing_key=os.getenv('APS_SIGNING_KEY', cls.signing_key),
        )
