import list_vms
import power_on_off_vm
 
# Listando as VM
'''
vms = list_vms.list_vm() 
for vm in vms:
    print(vm)
'''

# Ligando/Desligando VM
vmid = 'vm-7896'
vm_power = 'off'
power_on_off_vm.power_on_off(vmid,vm_power)