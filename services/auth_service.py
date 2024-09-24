import requests
from requests.auth import HTTPBasicAuth
from config import APIConfig

class AuthService:
    def __init__(self, api_config: APIConfig):
        self.api_config = api_config

    def get_access_token(self):
        url = f'{self.api_config.BASE_URL}/oauth2/token'
        data = {'grant_type': 'client_credentials'}
        response = requests.post(url, data=data, auth=HTTPBasicAuth(self.api_config.EMAIL, self.api_config.SENHA))
        if response.status_code == 200:
            return response.json()['access_token']
        else:
            raise Exception(f"Failed to get access token: {response.status_code}")
