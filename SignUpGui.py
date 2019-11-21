import PySimpleGUI as sg
import extensions as ext
from IGui import IGui
import getCheckedApp as app

def validateInput(input):
    if re.match("[\w.]+@[\a-zA-z]+(\.[a-z]+)+$", input['email']):
        print('email')
    if re.match(".{8,}", input['pass']):
        if input['pass'] == input['repass']:
            print('password')

def signUpLayout():
    return [[sg.Text('Email', size=(10, None)), sg.InputText(key='email', enable_events=True)], 
            [sg.Text('Password', size=(10, None)), sg.InputText(key='pass', enable_events=True)],
            [sg.Text('Company', size=(10, None)), sg.InputText(key='companay', enable_events=True)],
            [sg.Text('First Name', size=(10, None)), sg.InputText(key='fname', enable_events=True)],
            [sg.Text('Last Name', size=(10, None)), sg.InputText(key='lname', enable_events=True)],
            [sg.Button('Previous', key='btn_prev'), sg.Button('Next', key=('btn_next'))]]

class SignUpGui(IGui):
    def __init__(self):
        layout =   []
        row = []
        sg.change_look_and_feel('Topanga')
        row += [sg.Frame('Account Information', signUpLayout())]
        layout += [row]
        window = sg.Window('Create Account', layout)

    def getGui(self):
        return self.window

    def listen(self):
        
        while True:
            event, values = self.window.Read()
            if event is None:
                return 0
            elif event == 'btn_next':
                validateInput(values)
                return 1
            elif event == 'btn_previous':
                return -1