import os
import requests
import auth_vcenter

api_host = os.getenv('VCENTER_SERVER')  # Puxando das variáveis de ambiente

def power_on_off(vmid,vm_power):
    token = auth_vcenter.login_api_vmware() # Chamando a função que autentica no vCenter para obter o token
    if vm_power == 'off':
        url = f'https://{api_host}/rest/vcenter/vm/{vmid}/power/stop'
        message_power = f'VM {vmid} foi desligada!'
    elif vm_power == 'on':
        url = f'https://{api_host}/rest/vcenter/vm/{vmid}/power/start'
        message_power = f'VM {vmid} foi ligada!'        
    # Passando o token de sessão como parametro no header
    headers = {
        'Content-Type': 'application/json',
        'vmware-api-session-id': token
    }
    response = requests.post(url, headers=headers, verify=False)
    if response.status_code == 200:
        message = message_power
        print(message)
    elif response.status_code == 400:
        content = response.json()
        message = content['value']['messages'][0]['default_message']
        print(message)
    else:
        print(response.text)