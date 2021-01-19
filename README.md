# Script python3 para listar VMs utilizando API do vCenter

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
    - Execute o script
    ```sh
    python3 list_vms.py
    ```