import PySimpleGUI as sg
import extensions as ext

def createInstance(name, i):
    nameVM = name + 'x64v' + str(i)
    return [sg.Text(text = nameVM, font = '#ff3399', size=(10, 0)),
            sg.Text('Ram(Gb)'),
            sg.Slider(range = (4, ext.getRam()), default_value = 4,
                      orientation = 'horizontal', size=(10, 10), key = nameVM + '_memory'),
            sg.Text('CPU'),
            sg.Combo(list(range(2, ext.getCPU() + 1)), default_value = 2, key = nameVM + '_cpu'), 
            sg.Text('Hard_disk(Gb)'), 
            sg.InputText('256', size = (10, 30), key = nameVM + '_disk'),
            sg.Combo([1, 2, 3, 4], default_value = 1, key = nameVM + '_instance'), 
            sg.Button('Apps', key = nameVM + '_btn_apps'),
            sg.Button('Reset', key = nameVM + '_btn_reset')]
    #[sg.Checkbox('a'), sg.Checkbox('a'), sg.Checkbox('a')]

class OS:
    os = ''
    num = 0

def create(scr):
    instances = []
    values = scr[0].Values
    arr = []
    lstOs = ['win7','win10','ws']
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
    window = sg.Window('SetInstant', instances)
    return window

def destroy():
    window.Close()

lstVM = []

