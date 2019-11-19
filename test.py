import PySimpleGUI as sg

user = ''
passwd = ''
def sample_layout():
    return [[sg.Text('Username'), sg.InputText(metadata='Username', key='username', enable_events=True)], 
            [sg.Text('Password'), sg.InputText('Password', key='pass', enable_events=True)],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

layout =   []

row = []
sg.change_look_and_feel('Topanga')

row += [sg.Frame('Topanga', sample_layout())]
layout += [row]

window = sg.Window('Window Title', layout)
while True:
        event, values = window.Read()
        if event is None:
            break
        # else:
        #     if(event == 'username'):
        #     elif(event == 'pass')
print(user)
print(passwd)
