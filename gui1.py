import PySimpleGUI as sg


layout = [
    [sg.Checkbox('Windows 7', enable_events=True, key='win7', size=(15, 10)),
     sg.Text('Numbers of VMs'),
     sg.Spin([1, 2, 3, 4], initial_value=1, key='num_win7')],
    #  sg.Radio("Default", "mode1", default=True, key='default_win7'), 
    #  sg.Radio("Custom", "mode1", key='custom_win7'))],
    [sg.Checkbox('Windows 10', enable_events=True, key='win10', size=(15, 10)), 
     sg.Text('Numbers of VMs'),
     sg.Spin([1, 2, 3, 4], enable_events=True ,initial_value=1, key='num_win10')],
    [sg.Checkbox('Windows Server',  key='winsv', size=(15, 10)), 
     sg.Text('Numbers of VMs'), 
     sg.Spin([1, 2, 3, 4], initial_value=1, key='num_winsv')],
    [sg.Submit('Default', key='btn_default'), 
     sg.Submit('Next', key='btn_next')]
]


def create(scr):
    window = sg.Window('Config', layout)
    return window

def destroy():
    window.Close()
