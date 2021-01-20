import os
import requests
import auth_vcenter

api_host = os.getenv('VCENTER_SERVER')  # Puxando das variáveis de ambiente

token = auth_vcenter.login_api_vmware() # Chamando a função que autentica no vCenter para obter o token

def power_off(vmid):
    url = f'https://{api_host}/rest/vcenter/vm/{vmid}/power/stop'
    # Passando o token de sessão como parametro no header
    headers = {
        'Content-Type': 'application/json',
        'vmware-api-session-id': token
    }
    response = requests.post(url, headers=headers, verify=False)
    if response.status_code == 200:
        message = f'VM {vmid} foi desligada!'
        return message
    elif response.status_code == 400:
        content = response.json()
        message = content['value']['messages'][0]['default_message']
        return message
    else:
        print(response.text)

vmid = 'vm-7896'
poweroff = power_off(vmid)
print(poweroff)