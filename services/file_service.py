import requests
from config import APIConfig

class FileService:
    def __init__(self, api_config: APIConfig):
        self.api_config = api_config

    def send_file_to_4docs(self, file, access_token):
        url = f'{self.api_config.BASE_URL}/quick_parse/9fbc3a280191a0428e55c4a8fb235d8c'
        headers = {'Authorization': f'Bearer {access_token}'}
        files = {
            'file': (file.filename, file, 'application/pdf'),
            'json': (None, '{"callbackUrl":"https://api.4docs.cloud/v2/null","pipelineName":"energy","clientData":{"fatura_id":999}}', 'application/json')
        }

        response = requests.post(url, headers=headers, files=files)
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": "Non-JSON response" if response.status_code != 200 else "JSON Decode Error",
                "status_code": response.status_code,
                "content": response.text
            }
