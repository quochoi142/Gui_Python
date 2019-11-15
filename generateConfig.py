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


# def configData():
#     content={}
#     content['sandbox']={
#         'api': ':8121',
#         'receiver': 
#     }

with open("/home/hoivu/.hatch/data/sandbox.yaml", 'r') as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)