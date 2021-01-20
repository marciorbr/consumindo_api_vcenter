# Script python3 para listar e Delisgar VMs utilizando API do vCenter

* Para utilizar
    - Defina as variáveis de abiente com suas credenciais de acesso ao vcenter.

    ```sh
    export VCENTER_SERVER=10.10.10.100
    export VCENTER_USER=administrator@vsphere.local
    export VCENTER_PASS=password
    ```
    - Faça a instalação das bibliotecas 
    ```sh
    pip install requirements.txt
    ```
    - Execute o script para listar as VMs
    ```sh
    python3 list_vms.py
    ```
    - Execute o script para Desligar a VM. "OBS: Deve-se alterar a variável "vmid" para qual VM vai ser desligada, o vmid pode ser obtito no script que lista as VMs"
     ```sh
    python3 poweroff_vm.py
    ```