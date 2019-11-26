import getCheckedApp as app
from IGui import IGui
import PySimpleGUI as sg
import extensions as ext
from LicenseGui import LicenseGui


def createInstance(name, i):
    nameVM = name + 'x64v' + str(i)
    return [sg.Text(text=nameVM, font='#ff3399', size=(10, 0)),
            sg.Text('Ram(Gb)'),
            sg.Slider(range=(4, ext.getRam()), default_value=4,
                      orientation='horizontal', size=(10, 10), key=nameVM + '_memory'),
            sg.Text('CPU'),
            sg.Combo(list(range(2, ext.getCPU() + 1)),
                     default_value=2, key=nameVM + '_cpu'),
            sg.Text('Hard_disk(Gb)'),
            sg.InputText('256', size=(10, 30), key=nameVM + '_disk'),
            sg.Combo([1, 2, 3, 4], default_value=1, key=nameVM + '_instance'),
            sg.Button('Apps', key=nameVM + '_btn_apps'),
            sg.Button('Reset', key=nameVM + '_btn_reset')]


class OS:
    os = ''
    num = 0


defaultValues = {
    'memory': 2,
    'cpu': 2,
    'disk': 256,
    'instance': 1
}

lstOs = ['win7', 'win10', 'ws']


class ConfigVMsGui(IGui):
    def __init__(self, scr):
        instances = []
        self.temp=values = scr[0].Values
        arr = []
        for os in lstOs:
            if values[os] is True:
                x = OS()
                x.os = os
                x.num = values[os + '_num']
                arr.append(x)
        for i in arr:
            for j in range(1, i.num + 1):
                # nameVM = i.os + 'x64v' + str(j)
                # lstVM = lstVM.append(nameVM)
                instances.append(createInstance(i.os, j))

            # instances.append(createApp())
        instances.append([sg.Button('Previous', key='btn_prev'),
                          sg.Button('Next', key=('btn_next'))])
        self.window = sg.Window('SetInstant', instances, return_keyboard_events=True)
        self.lstApps = {}

    def getGui(self):
        return self.window

    def __check__(self):
        values = self.temp

        arr = []
        for os in lstOs:
            if values[os] is True:
                x = OS()
                x.os = os
                x.num = values[os + '_num']
                arr.append(x)
        for i in arr:
            for j in range(1, i.num + 1):
                key=i.os + 'x64v' + str(j)
                if key in self.lstApps:
                    if any('office' in item for item in self.lstApps[key]):
                        return True
        return False

    def listen(self):
        value = {}
        while True:
            event, values = self.window.Read()
            self.Values = values
            # print(values)
            lstApps = self.lstApps
            # print(values)
            if event is not None:
                key = event.split('_')[0]
            # print(key)
            if event is None:
                return 0
            elif event == 'btn_next':
                if self.__check__() == True:
                    self.license=LicenseGui()
                    if self.license.listen()==1:
                        self.license.getGui().Close()
                return 1
                
                
            elif event == 'btn_prev':
                return -1
            elif 'btn_apps' in event:
                if key in lstApps.keys():
                    lstApps[key] = app.getApps(lstApps[key])
                else:
                    lstApps[key] = app.getApps([])
                self.lstApps = lstApps
            elif 'btn_reset' in event:
                lstValues = ['memory', 'cpu', 'disk', 'instance']
                for value in lstValues:
                    if value in defaultValues.keys():
                        self.window.FindElement(
                            key + '_' + value).Update(value=defaultValues[value])
                del lstApps[key]
