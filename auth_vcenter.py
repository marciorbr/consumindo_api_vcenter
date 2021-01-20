import os
import requests
from requests.auth  import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # Desabilitando Warning cetificate invalide

username = os.getenv('VCENTER_USER')    # Puxando das variáveis de ambiente
password = os.getenv('VCENTER_PASS')    # Puxando das variáveis de ambiente
api_host = os.getenv('VCENTER_SERVER')  # Puxando das variáveis de ambiente
ENDPOINT_SESSION = f'https://{api_host}/rest/com/vmware/cis/session'    # Endpoint de autenticação da API


# Function autenticação na API vMware
def login_api_vmware():
    url = ENDPOINT_SESSION  # Pegando variável GLOBAL e utilizando na função
    # Realizando autenticação na API
    response = requests.post(url, auth=(username, password), verify=False)
    if response.status_code == 200:
        content = response.json()
        token = content['value']
        return token