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
        self.progress=0
        self.scr=scr
        self.done=False
        self.err=False
        
    def getGui(self):
        return self.window

    def __install__(self, scr, password, src):

        # # permission
        # p=sp.run('echo {} | echo -S 1'.format(password), shell=True,stdout=sp.PIPE)
        # if p.stdout!= b'1\n':
        #     self.err=True
        #     return

        #prepare environment
        #sp.call('./Install/Step1.sh')
        genYaml.config(scr)
        # install package and kill processes
        sp.call("./Intall/Step2.sh")
        self.updateProgress(10)
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
                self.updateProgress(10)
            sp.call('./Install/Download.sh')
        else:
            sp.call('sudo cp {}/* {}'.format(src,
                                             etx.homedir+'/.hatch/resources/'))

            for i in range(0, 5):
                time.sleep(2)
                self.updateProgress(10)

        gen.configData(scr)
        sp.call('./Intall/Step3.sh')
        # create VMs
        files = etx.getAllfile('~/.hatch/config', '.yaml')
        leng = len(files)
        for file in files:
            sp.call(['./Install/InstallVm.sh',file])
            self.updateProgress(1/leng*10)

        subprocess.call("./Intall/Step4.sh")
        # Create account Postgres
        subprocess.call("./Intall/Step5.sh")
        self.done = True

    def updateProgress(i):

        for j in range(1, i):
            time.sleep(1)
            self.progress += j
            self.getGui().find_element('progressbar').UpdateBar(self.progress)

    def listen(self):

        while 1:
            events, values = self.window.Read(timeout=10)
            if events is None:

                return 1
            if events == 'btn_ins':
                # password=confirm_Password()
                # if password!="":                
                    
                    t1= threading.Thread(target=self.__install__,args=(self.scr,password,None,))
                    t1.start()
                    t1.join()
                    self.window.find_element('btn_ins').Update(disabled=True)
            if self.done == True:
                break
            if self.err==True:
                self.window.find_element('btn_ins').Update(disabled=False)
        return 1
