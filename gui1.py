import PySimpleGUI as sg
arr = ['a', 'b', 'v']


def createApp(name):
    return [sg.Checkbox(name, size=(10, 2))]


ColumnAppWin7 = [
    createApp(i) for i in arr
]


Win7 = [sg.Checkbox('Windows 7', enable_events=True, key='win7', size=(15, 10)), sg.Text('Numbers of instant'), sg.Spin([1, 2, 3, 4], initial_value=1),
        sg.Column(ColumnAppWin7, vertical_scroll_only=True, scrollable=True)]

layout = [

    [sg.Checkbox('Windows 7', enable_events=True, key='win7', size=(15, 10)), sg.Text('Numbers of instant'), sg.Spin([1, 2, 3, 4], initial_value=1),
     sg.Radio("Default", "mode1",default=True), sg.Radio("Custom", "mode1")],
    [sg.Checkbox('Windows 10', size=(15, 10)), sg.Text(
        'Numbers of instant'), sg.Spin([1, 2, 3, 4], initial_value=1),
     sg.Radio("Default", "mode2",default=True), sg.Radio("Custom", "mode2")],
    [sg.Checkbox('Windows Server', size=(15, 10)), sg.Text(
        'Numbers of instant'), sg.Spin([1, 2, 3, 4], initial_value=1),
     sg.Radio("Default", "mode3",default=True), sg.Radio("Custom", "mode3")],
    [sg.Submit('Next',key='Next')]
]

window = sg.Window('Config', layout)
window_Next=False

while True:
    event, values= window.Read()
    if event is None: 
        break
  

        
window.Close()
