import PySimpleGUI as sg
<<<<<<< HEAD
# import gui2
arr = ['a', 'b', 'v']


def createApp(name):
    return [sg.Checkbox(name, size=(10, 2))]


ColumnAppWin7 = [
    createApp(i) for i in arr
]


Win7 = [sg.Checkbox('Windows 7', enable_events=True, key='win7', size=(15, 10)), sg.Text('Numbers of instant'), sg.Spin([1, 2, 3, 4], initial_value=1),
        sg.Column(ColumnAppWin7, vertical_scroll_only=True, scrollable=True)]
=======
>>>>>>> origin/dev

layout = [
    [sg.Checkbox('Windows 7', enable_events = True, key = 'win7', size=(15, 10)),
     sg.Text('Numbers of VMs'),
     sg.Spin([1, 2, 3, 4], initial_value = 1, key = 'win7_num')],
    #  sg.Radio('Default', 'mode1', default=True, key = 'default_win7'), 
    #  sg.Radio('Custom', 'mode1', key = 'custom_win7'))],
    [sg.Checkbox('Windows 10', enable_events = True, key = 'win10', size = (15, 10)), 
     sg.Text('Numbers of VMs'),
     sg.Spin([1, 2, 3, 4], enable_events = True ,initial_value = 1, key = 'win10_num')],
    [sg.Checkbox('Windows Server',  key = 'ws', size=(15, 10)), 
     sg.Text('Numbers of VMs'), 
     sg.Spin([1, 2, 3, 4], initial_value = 1, key = 'ws_num')],
    # [sg.Submit('Default', key = 'btn_default')],
    [sg.Submit('Next', key = 'btn_next')]
]

<<<<<<< HEAD
# print(layout)
window = sg.Window('Config', layout)
# window_Next=False
# exec('gui2.py')
while True:
    event, values= window.Read()
    if event is None: 
        break
  
=======
def create(scr):
    window = sg.Window('Config', layout)
    return window
>>>>>>> origin/dev

def destroy():
    window.Close()
