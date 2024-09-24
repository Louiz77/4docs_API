import requests

BASE_URL = 'https://api.4docs.cloud/v2'
EMAIL = 'jean.santos@itfacil.com.br'
SENHA = 'vfxotgjphdvafiby'

def get_access_token():
    url = f'{BASE_URL}/oauth2/token'
    data = {'grant_type': 'client_credentials'}
    response = requests.post(url, data=data, auth=(EMAIL, SENHA))
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception(f"Failed to get access token: {response.status_code}")

def send_file_to_4docs(file, access_token):
    url_2 = f'{BASE_URL}/quick_parse/9fbc3a280191a0428e55c4a8fb235d8c'

    headers = {'Authorization': f'Bearer {access_token}'}

    files = {
        'file': (file.filename, file, 'application/pdf'),
        'json': (None, '{"callbackUrl":"https://api.4docs.cloud/v2/null","pipelineName":"energy","clientData":{"fatura_id":999}}', 'application/json')
    }

    response = requests.post(url_2, headers=headers, files=files)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": "Non-JSON response" if response.status_code != 200 else "JSON Decode Error",
            "status_code": response.status_code,
            "content": response.text
        }