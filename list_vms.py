import os
import requests
import auth_vcenter

api_host = os.getenv('VCENTER_SERVER')  # Puxando das variáveis de ambiente

def list_vm ():
    token = auth_vcenter.login_api_vmware() # Chamando a function e pegando o token de sessão
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
