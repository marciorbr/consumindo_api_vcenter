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
    else:
        print(f'Erro de conexão')

def list_vm (token):
    url = f'https://{api_host}/rest/vcenter/vm'
    # Passando o token de sessão como parametro no header
    headers = {
        'Content-Type': 'application/json',
        'vmware-api-session-id': token
    }
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        vms = []    # Criando uma lista vazia para add o dicionário personalizado
        content = response.json()
        for vm in content['value']:
            temp_dict = {}  # Criando um dicionário vazio
            # Criando dicionário perzonalizado
            temp_dict['vm_id']=vm['vm']
            temp_dict['vm_name']=vm['name']
            temp_dict['vm_state']=vm['power_state']
            temp_dict['vm_cpu']=vm['cpu_count']
            temp_dict['vm_memory']=vm['memory_size_MiB']
            vms.append(temp_dict) # Add dicionário perzonalizado a lista de vms
        return vms
    else:
        print(f'Erro na requisição')

token = login_api_vmware() # Chamando a function e pegando o token de sessão 
vms = list_vm(token) # Chamando a function e passando o token pego acima 
# Listando as VM 
for vm in vms:
    print(vm)
