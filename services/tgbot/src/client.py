import requests
import logging

from config.config import Config


class BackendClient:
    def __init__(self, url=Config.SERVICE_URL):
        self.url = url

    def get(self, request_postfix, json_data):
        try:
            response = requests.get(url=f'{self.url}{request_postfix}', params=json_data)
        except Exception as e:
            response = None
            logging.error(f'e - {e}')

        if response is not None and response.status_code == 200:
            return response.json()
        else:
            return 'failed'

    def ping(self):
        return self.get(request_postfix='/ping', json_data={})

    def get_english_word(self, json_data):
        return self.get(request_postfix='/v1/english', json_data=json_data)
