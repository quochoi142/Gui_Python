import getpass
import extensions as etx
import generateConfig as gen

lstOs = [
    {'os': 'win7', 'name': 'windows7', 'arch': 'x64', 'from': 10, 'to': 39, 'num': 0},
    {'os': 'win10', 'name': 'windows10', 'arch': 'x64', 'from': 100, 'to': 129, 'num': 0},
    {'os': 'ws', 'name': 'windowsserver2016', 'arch': 'x64', 'from': 70, 'to': 99, 'num': 0}
]


def config(scr):
    scr0 = scr[0].Values
    scr1 = scr[1].Values
    lstAppsDefault =  ['schtasks', 'setres', 'windows', 'wallpaper-fetch', 'cppredist',
                'dotnet472', 'mscorsvw', 'schtasks', 'ps1logging', 'patchandgo', 'finalize']
    lstApps = scr[1].lstApps
    print(lstApps)
    for os in lstOs:
        # print(scr0[os['os']])
        if scr0[os['os']] == True:
            os['num'] = scr0[os['os']+'_num']
    # print(lstOs)              //print list OS config
    for os in lstOs:
        for i in range(1, os['num']+1):
            id = os['os'] + os['arch'] + 'v' + str(i)
            content = {}
            user = getpass.getuser()
            content['Storage_dir'] = etx.homedir + '/.hatch/vmdata/storage'
            content['temp_dir'] = etx.homedir + '/.hatch/vmdata/scratch'
            content['data_dirs'] = ['./resources']
            content['script_dirs'] = ['./scripts']
            content['bridge'] = 'br0'
            content['bridge_ip'] = '10.6.0.1/24'
            content['id'] = id
            content['os'] = os['name']
            content['os_product_version'] = 'professional'
            content['arch'] = os['arch']
            content['iso_file'] = 'win7ultimate.iso'
            content['machine'] = {
                'cpu_cores': scr1[id + '_cpu'],
                'memory': str(int(scr1[id+'_memory'])) + 'G',
                'disk': str(scr1[id+'_disk']) + 'G'
            }
            # print(lstApps[id])
            if id in lstApps.keys():
                lstApps[id].extend(lstAppsDefault)
            else:
                lstApps[id] = lstAppsDefault
            lstApps[id].append(os['name'])
            print(lstApps)
            content['scripts'] = []
            for app in lstApps[id]:
                # print(app)
                content['scripts'].append({'name': app})
            content['instances'] = []
            for j in range(1, scr1[id+'_instance'] + 1):
                ins = {
                    'ip': '10.6.0.'+str(os['from']+j) + '/24',
                    'interface': 'tap' + str(os['from'] + j),
                    'vnc_port': 11000 + os['from'] + j
                }
                content['instances'].append(ins)
            gen.generateConfig(content, id)
            # print(content)
