import PySimpleGUI as sg


layout = [

    [sg.Checkbox('Windows 7', enable_events=True, key='win7', size=(15, 10)),
     sg.Text('Numbers of VMs'),
     sg.Spin([1, 2, 3, 4], initial_value=1, key='num_win7'),
     sg.Radio("Default", "mode1", default=True), sg.Radio("Custom", "mode1")],
    [sg.Checkbox('Windows 10', enable_events=True, key='win10', size=(15, 10)), sg.Text(
        'Numbers of VMs'), sg.Spin([1, 2, 3, 4], enable_events=True ,initial_value=1, key='num_win10'),
     sg.Radio("Default", "mode2", default=True), sg.Radio("Custom", "mode2")],
    [sg.Checkbox('Windows Server',  key='winsv', size=(15, 10)), sg.Text(
        'Numbers of VMs'), sg.Spin([1, 2, 3, 4], initial_value=1, key='num_winsv'),
     sg.Radio("Default", "mode3", default=True), sg.Radio("Custom", "mode3")],
    [sg.Submit('Next', key='btn_next')]
]


def create(scr):
    window = sg.Window('Config', layout)
    return window


def destroy():
    window.Close()
