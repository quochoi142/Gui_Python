import oyaml as yaml
import os.path
import getpass
import extensions as etx
from collections import OrderedDict


def generateConfig(content,name):
    if os.path.isfile(etx.homedir+'/Desktop/' +name + '.yaml'):
        os.remove(etx.homedir+'/Desktop/'+ name + '.yaml')

    with open(etx.homedir+'/Desktop/' +name + '.yaml', 'w') as outfile:
        try:
          
            yaml.dump(content, outfile, default_flow_style=False)
        except yaml.YAMLError as exc:
            print(exc)


def configData():
    content={}
    content['sandbox']={
        'api': ':8121',
        'receiver': ':41234',
        'display_addr':etx.getIp()
    }
    content['machines']=[]
    VMs=etx.getAllfile(etx.homedir+'/.hatch/config','.yaml')
    for vm in VMs:
        temp={}
        temp['conf']=etx.homedir+'/.hatch/vmdata/storage/'+vm+'/instance_0.vm'
        temp['tags']=



# with open('/home/hoivu/.hatch/data/sandbox.yaml', 'r') as stream:
#     try:
#         x=yaml.safe_load(stream)
#         print(x)
#     except yaml.YAMLError as exc:
#         print(exc)

