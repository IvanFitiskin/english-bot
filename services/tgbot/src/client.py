import requests

from common.config import Config


class BackendClient:
    def __init__(self, host=Config.SERVICE_HOST, port=Config.SERVICE_PORT):
        self.url = '{0}:{1}'.format(host, port)

    def get(self, request_postfix, json_data):
        try:
            response = requests.get(self.url + request_postfix, params=json_data)
        except Exception as e:
            response = None

        if response is not None and response.status_code == 200:
            return response.json()
        else:
            return 'failed'

    def get_english_word(self, data):
        return self.get('/v1/english', data)
