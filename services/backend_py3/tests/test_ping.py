import requests

from config.backend_py3 import Config

SERVICE_URL = Config.SERVICE_URL


def test_ping():
    assert requests.get(f'{SERVICE_URL}/ping').status_code == 200
