import os
import requests
import auth_vcenter
import power_on_off_vm
import json

api_host = os.getenv('VCENTER_SERVER')  # Puxando das variáveis de ambiente

def update_cpu(vmid,cpu):
    token = auth_vcenter.login_api_vmware()
    url = f'https://{api_host}/rest/vcenter/vm/{vmid}/hardware/cpu'
    # Passando o token de sessão como parametro no header
    headers = {
        'Content-Type': 'application/json',
        'vmware-api-session-id': token
    }
    data = {
        "spec":{
            "cores_per_socket": cpu,
            "count": cpu
        }
    }
    power_on_off_vm.power_on_off(vmid,vm_power='off')
    response = requests.patch(url, headers=headers, data=json.dumps(data), verify=False)

    if response.status_code == 200:
        message = f'VM {vmid} atualizada para {cpu} CPU.'
        print(message)
    else:
        content = response.json()
        message = content['value']['messages'][0]['default_message']
        print(message)
    power_on_off_vm.power_on_off(vmid,vm_power='on')