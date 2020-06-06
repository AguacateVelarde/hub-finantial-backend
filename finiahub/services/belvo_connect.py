import requests
from requests.auth import HTTPBasicAuth


class Belvo:
    def __init__(self, secret_id, secret_password):
        self.secret_id = secret_id
        self.secret_password = secret_password

    def list_institutions(self):
        response = requests.get('https://api.belvo.co/api/institutions/',
                                auth=HTTPBasicAuth(self.secret_id, self.secret_password))
        return response.json()
