import PySimpleGUI as sg

layout = [
    [sg.Checkbox('Windows 7', default=True, key = 'win7', size=(15, 10)),
     sg.Text('Numbers of VMs'),
     sg.Spin([1, 2, 3, 4], initial_value = 1, key = 'win7_num')],
    #  sg.Radio('Default', 'mode1', default=True, key = 'default_win7'), 
    #  sg.Radio('Custom', 'mode1', key = 'custom_win7'))],
    [sg.Checkbox('Windows 10', default=True, key = 'win10', size = (15, 10)), 
     sg.Text('Numbers of VMs'),
     sg.Spin([1, 2, 3, 4], enable_events = True ,initial_value = 1, key = 'win10_num')],
    [sg.Checkbox('Windows Server', default=True,  key = 'ws', size=(15, 10)), 
     sg.Text('Numbers of VMs'), 
     sg.Spin([1, 2, 3, 4], initial_value = 1, key = 'ws_num')],
    # [sg.Submit('Default', key = 'btn_default')],
    [sg.Submit('Next', key = 'btn_next')]
]
    # print(selectScripts)

def create(scr):
    window = sg.Window('Config', layout)
    return window

def destroy():
    window.Close()
