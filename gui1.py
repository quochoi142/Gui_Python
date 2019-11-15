import PySimpleGUI as sg


layout = [

    [sg.Checkbox('Windows 7', key='win7', size=(15, 10), default=True),
     sg.Text('Numbers of VMs'),
     sg.Spin([1, 2, 3, 4], initial_value=1, key='win7_num')],
    [sg.Checkbox('Windows 10', enable_events=True, key='win10', size=(15, 10), default=True), sg.Text(
        'Numbers of VMs'), sg.Spin([1, 2, 3, 4], enable_events=True, initial_value=1, key='win10_num')],
    [sg.Checkbox('Windows Server',  key='ws', size=(15, 10), default=True), sg.Text(
        'Numbers of VMs'), sg.Spin([1, 2, 3, 4], initial_value=1, key='ws_num')
     ],
    [sg.Submit('Next', key='btn_next')]

]


def create(scr):
    window = sg.Window('Config', layout)
    return window


def destroy():
    window.Close()
