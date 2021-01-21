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
    - Para executar os scripts remova os ''' para a função que for utilizar no arquivo main.py depois chame o script
    ```sh
    python3 main.py
    ```