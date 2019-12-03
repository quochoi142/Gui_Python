import PySimpleGUI as sg
import extensions as ext
from IGui import IGui
import getCheckedApp as app
import re

def validateInput(input):
    if re.match("[\w.]+@[\a-zA-z]+(\.[a-z]+)+$", input['email']):
        print('email')
    if re.match(".{8,}", input['password']):
        if input['password'] == input['repassword']:
            print('password')

def createAccountLayout():
    return [[sg.Text('Email', size=(10, None)), sg.InputText(key='email', enable_events=True)], 
            [sg.Text('Password', size=(10, None)), sg.InputText(key='password', enable_events=True)],
            [sg.Text('Confirm password', size=(10, None)), sg.InputText(key='repassword', enable_events=True)],
            [sg.Text('Phone number', size=(10, None)), sg.InputText(key='phone', enable_events=True)],
            [sg.Text('Company', size=(10, None)), sg.InputText(key='company', enable_events=True)],
            [sg.Text('First Name', size=(10, None)), sg.InputText(key='fname', enable_events=True)],
            [sg.Text('Last Name', size=(10, None)), sg.InputText(key='lname', enable_events=True)],
            [sg.Button('Previous', key='btn_previous'), sg.Button('Next', key=('btn_next'))]]

class CreateAccountGui(IGui):
    def __init__(self, scr):
        layout =   []
        row = []
        sg.change_look_and_feel('Topanga')
        row += [sg.Frame('Account Information', createAccountLayout())]
        layout += [row]
        self.window = sg.Window('Create Account', layout)

    def getGui(self):
        return self.window

    def listen(self):
        while True:
            event, values = self.window.Read()
            if event is None:
                return 0
            elif event == 'btn_next':
                validateInput(values)
                self.values=values
                return 1
            elif event == 'btn_previous':
                return -1