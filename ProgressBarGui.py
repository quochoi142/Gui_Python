import PySimpleGUI as sg
from IGui import IGui
import subprocess as sp
import getInforScreen as genYaml
import generateConfig as gen
import extensions as etx
import time
import threading


def confirm_Password():
    layout = [
        [sg.Text("Password OS"), sg.InputText(
            "", password_char='*', key='pass')],
        [sg.Button("Confirm", key='btn_confirm')]
    ]
    win = sg.Window('Password', layout)
    while 1:
        events, values = win.Read()
        if events is None:
            win.Close()
            return ""
        if events == 'btn_confirm':
            if values['pass'] != "":
                win.Close()
                return values['pass']


class ProgressBarGui(IGui):
    def __init__(self, scr):
        layout = [
            [sg.ProgressBar(max_value=100, orientation='horizontal', size=(20, 20),
                            key='progressbar')],

            [sg.Button('Install', key='btn_ins')]

        ]
        self.window = sg.Window('Progress', layout)
        self.progress = 0
        self.scr = scr
        self.done = False
        self.err = False

    def getGui(self):
        return self.window

    def __install__(self, scr, password, src):
        user=etx.username
        print(user)
        # permission
        p = sp.run('echo {} | sudo -S echo 1'.format(password),
                   shell=True, stdout=sp.PIPE)
        if p.stdout != b'1\n':
            self.err = True
            return
        print('permission')
        # prepare environment
        sp.call(['sudo',"./Install/Step1.sh",user])
        

        # install package and kill processes
        sp.call(['sudo',"./Install/Step2.sh",user])
        self.progress+=20
        print('install package')
        # get resource
        if src is None:
            softs = [
                'sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/tongqing_liu_opswat_com/EV0hanqY-FFOg9zAOjiVQWMBWoqXEyJ5zGsOytNGki5smw?download=1 -O $HATCHING/resources/win7ultimate.iso -q --show-progress',
                'sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/tongqing_liu_opswat_com/Edr41t0uY7NBpmG5MjzP-ngBn6rMyLm0VGWAUgx3NJiRkA?download=1 -O $HATCHING/resources/Win10_1703_English_x64.iso -q --show-progress',
                'sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/tongqing_liu_opswat_com/ERYd0WjCl49JpiUgyOOSbnYB-2Ow2mqc7Oq0icenM1sM4g?download=1 -O $HATCHING/resources/en_windows_server_2016_x64_dvd_9718492.iso -q --show-progress',
                'sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/tongqing_liu_opswat_com/EWKVaiHETXlMkXSXE5BuBtMBhkxfj4wtTTvl2rthvP2wxw?download=1 -O $HATCHING/resources/en_office_professional_plus_2010_x86_x64_dvd_515529.iso -q --show-progress',
                'sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/tongqing_liu_opswat_com/EUpS4SnVdtNLvlv8mfxdO60Bnni8OHG7LRzCgmDCG4i_1w?download=1 -O $HATCHING/resources/ubuntu-1804-amd64.qcow2 -q --show-progress',
                'sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/tai_vu_opswat_com/EZYZuDtq8jZAp108Ot3F-HQBNHgP9Op2tauM2BYheQwpXg?download=1 -O $HATCHING/resources_tmp.zip -q --show-progress',
                'sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/thi_nguyen_opswat_com/EbmvfeZp6aRKnXhb1Z00hBUBkGUmwOc-JapMQMYNntQJBQ?download=1 -O $HATCHING/resources_tmp2.zip -q --show-progress',
                'sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/thi_nguyen_opswat_com/EYO8YTWofWhLnKBPDPlhz50BpGmy52ocvYQqXXdRth3eGA?download=1 -O $HATCHING/Resource_for_1st_integration.zip -q --show-progress',
                'sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/thi_nguyen_opswat_com/EfCgzTh8OARNvCX1UFE_Y2wBHsJGzi8zHvoUK6icolgetQ?download=1 -O $HATCHING/resources/CentOS-7-x86_64-Minimal-1810.iso -q --show-progress',
                'sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/thi_nguyen_opswat_com/EdBqg-HF6ElJqjllW086xVEB0diiooZ8TJ-NPtxWrXcVOA?download=1 -O $HATCHING/resources/Office.zip -q --show-progress'
            ]
            for i in range(0, 5, 2):
                sp.run(softs[i], shell=True)
                sp.run(softs[i+1], shell=True)
                self.progress+=10
            sp.call(['sudo',"./Install/Download.sh",user])
        else:
            sp.call(['sudo','cp',src,'/home/'+user+'/.hatch/resources/'])
            
            for i in range(0, 5):
                time.sleep(2)
                self.progress+=10
        print('get resources')

        gen.prepareConfig()
        genYaml.config(scr)
        print('generate YAML file')
        print('config vm')
        gen.configData()
        print('config sanbox.yaml')

        sp.call(['sudo',"./Install/Step3.sh",user])
        print('config')

        # create VMs
        files = etx.getAllfile('/home/'+user+'/.hatch/config', '.yaml')
        leng = len(files)
        for file in files:
            sp.call(['sudo','./Install/InstallVm.sh',user,'/home/'+user+'/.hatch/config/'+file+'.yaml'])
            self.progress+=1/leng*10
        print('create VMs')

        sp.call(['sudo',"./Install/Step4.sh",user])
        print('set network')

        account = src[2].values
        sp.call(['sudo','./Install/CreateAccount.sh',
            account['company'], account['email'], account['fname'], account['lname'], account['password'], account['phone']])
        print('create account')

        sp.call(['sudo',"./Install/Step5.sh",user])
        print('Done')

        self.done = True

    def updateProgress(self,i):

            self.window['progressbar'].UpdateBar(self.progress)

    def listen(self):

        while 1:
            events, values = self.window.Read(timeout=10)
            if events is None:

                return 1
            if events == 'btn_ins':
                password = confirm_Password()
                if password != "":

                    t1 = threading.Thread(
                        target=self.__install__, args=(self.scr, password, '/home/'+etx.username+'/Desktop/Shared/Resources',))
                    t1.start()
                    t1.join()
                    self.window.find_element('btn_ins').Update(disabled=True)
            self.updateProgress(self.progress)
            if self.done == True:
                break
            if self.err == True:
                self.window.find_element('btn_ins').Update(disabled=False)
        return 1
