import oyaml as yaml
import os.path
import getpass
import extensions as etx
from collections import OrderedDict

# with open("/home/hoivu/.hatch/hoi.yaml", 'r') as stream:
#     try:
#         x=yaml.safe_load(stream)
#         print(x)
#     except yaml.YAMLError as exc:
#         print(exc)

<<<<<<< HEAD
def definePath():
    return '/.hatch/' + name
    
=======

>>>>>>> origin/hoi
def generateConfig(content,name):
    if os.path.isfile(etx.homedir + '/.hatch/' + name + '.yaml'):
        os.remove(etx.homedir + '/.hatch/'+ name + '.yaml')

    with open(etx.homedir + '/.hatch/' + name + '.yaml', 'w') as outfile:
        try:
            yaml.dump(content, outfile, default_flow_style=False)
        except yaml.YAMLError as exc:
            print(exc)

def configData():
    content = {}
    content['sandbox'] = {
        'api': ':8121',
        'receiver': ':41234',
        'display_addr': etx.getIp()
    }
    content['machinery'] = []
   # content['machinery'].append()
    machine = {
        'platform': 'qemu',
        'interface': 'br0',
        'ip': '10.6.0.1'}
    machine['machines'] = {}
    VMs = etx.getAllfile(etx.homedir+'/.hatch/vmdata/storage', '.yaml')
    for vm in VMs:
        if os.path.exists(etx.homedir+'/.hatch/vmdata/storage/'+vm+'/instance_0.vm'):
            temp = {}
            temp['conf'] = etx.homedir + \
                '/.hatch/vmdata/storage/'+vm+'/instance_0.vm'
            temp['tags'] = parseYaml(
                etx.homedir+'/.hatch/vmdata/storage/'+vm+'.yaml')
            temp['tags'].append('x64')
            machine['machines'][vm] = temp
    content['machinery'].append(machine)
    generateConfig(content,'data/sandbox')

def parseYaml(path):
    with open(path, 'r') as stream:
        try:
            x = yaml.safe_load(stream)
            return x['tags']
        except yaml.YAMLError as exc:
            print(exc)


