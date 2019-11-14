
import yaml

with open("/home/hoivu/Desktop/hoi.yaml", 'r') as stream:
    try:
        x=yaml.safe_load(stream)
        print(x)
    except yaml.YAMLError as exc:
        print(exc)


def generateConfig(name,src):
    content = {
        'storage_dir': '/home/user_name/.hatch/vmdata/storage',
        'temp_dir': '/home/user_name/.hatch/vmdata/scratch',
        'data_dirs': [ './resources' ],
        'script_dirs': [ './scripts' ],
        'bridge': 'br0',
        'bridge_ip': '10.6.0.1/24',

        'id': 'win7x64ACV',
        'os': 'windows7',
        'os_product_version': 'professional',
        'arch': 'x64',
        'iso_file': 'win7ultimate.iso',
        'machine':{
            'cpu_cores': 2,
            'memory': '4G',
            'disk': '256G'
        },
        'scripts': [
            #Required
            {'name': 'schtasks'},
            {'name': 'setres', 'vars': {'width': 1280, 'height': 720}},
            {'name': 'windows'},
            {'name': 'windows7'},
            {'name': 'wallpaper-fetch'},
            {'name': 'cppredist'},
            {'name': 'dotnet472'},
            {'name': 'mscorsvw'},
            {'name': 'schtasks'},
            {'name': 'ps1logging'},
            {'name': 'patchandgo'},
            {'name': 'finalize'},

            # Recommended
            #{'name': 'adobe9'}
            #{'name': 'java7-jdk'}
            #{'name': 'ie11'}
            #{'name': 'chrome'}
            #{'name': 'firefox'}
            #{'name': 'office2010', 'vars': {'licenseKey': 'GCCVP-793B7-92C6G-KJ4CD-98RYD'}}

            #Optional
            #{'name': '7zip'}
            #{'name': 'python2'}
            #{'name': 'vlc'}
            #{'name': 'ccleaner'}
            #{'name': 'gimp'}
            #{'name': 'random-files'}
        ],
         
          
        'instances':
            {'ip': '10.6.0.11/24', 'interface': 'tap11', 'vnc_port': 11011}
    } 
    with open('/home/hoivu/Desktop/'+name+'.yaml', 'w') as outfile:
        try:
            yaml.dump(content, outfile, default_flow_style=False,) 
        except yaml.YAMLError as exc:
        print(exc)  

generateConfig('hoi',12)