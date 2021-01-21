import list_vms
import power_on_off_vm
import update_cpu
 
# Listando as VM
'''
vms = list_vms.list_vm() 
for vm in vms:
    print(vm)
'''

# Ligando/Desligando VM
'''
vm_power = 'off'
vmid = 'vm-7896'
power_on_off_vm.power_on_off(vmid,vm_power)
'''

# Alterando quantidade CPU da VM
'''
vmid = 'vm-7896'
cpu = 3
update_cpu.update_cpu(vmid, cpu)
'''