from aps.platform import RuntimeConfig


def test_runtime_config_defaults():
    config = RuntimeConfig()

    assert config.app_name == 'APS Professional Suite'
    assert config.version == '0.3.0'
    assert config.environment == 'development'
    assert config.database_path == 'data/aps.sqlite3'


def test_runtime_config_from_environment(monkeypatch):
    monkeypatch.setenv('APS_APP_NAME', 'APS Test')
    monkeypatch.setenv('APS_VERSION', '10.0.0')
    monkeypatch.setenv('APS_ENVIRONMENT', 'test')
    monkeypatch.setenv('APS_DATABASE_PATH', 'tmp/test.sqlite3')
    monkeypatch.setenv('APS_SIGNING_KEY', 'test-key')

    config = RuntimeConfig.from_env()

    assert config.app_name == 'APS Test'
    assert config.version == '10.0.0'
    assert config.environment == 'test'
    assert config.database_path == 'tmp/test.sqlite3'
    assert config.signing_key == 'test-key'
