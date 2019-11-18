import oyaml as yaml
import os.path
import getpass
import extensions as etx
from collections import OrderedDict

# with open("/home/hoivu/Desktop/hoi.yaml", 'r') as stream:
#     try:
#         x=yaml.safe_load(stream)
#         print(x)
#     except yaml.YAMLError as exc:
#         print(exc)

def generateConfig(content,name):
    if os.path.isfile(etx.homedir + '/Desktop/' + name + '.yaml'):
        os.remove(etx.homedir + '/Desktop/'+ name + '.yaml')

    with open(etx.homedir + '/Desktop/' + name + '.yaml', 'w') as outfile:
        try:
            yaml.dump(content, outfile, default_flow_style=False)
        except yaml.YAMLError as exc:
            print(exc)

