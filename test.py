<<<<<<< HEAD
import PySimpleGUI as sg
import re

user = ''
passwd = ''
def loginLayout():
    return [[sg.Text('Username'), sg.InputText(metadata='Username', key='username', enable_events=True)], 
            [sg.Text('Password'), sg.InputText('Password', key='pass', enable_events=True)],
            [sg.Button('Ok'), sg.Button('Cancel')]]

def signupLayout():
    return [[sg.Text('Email', size=(18, None), pad=(None, 8)), sg.InputText(key='email', enable_events=True)], 
            [sg.Text('Password', size=(18, None), pad=(None, 8)), sg.InputText(key='pass', enable_events=True, password_char='*')],
            [sg.Text('Confirm Password', size=(18, None), pad=(None, 8)), sg.InputText(key='repass', enable_events=True, password_char='*')],
            [sg.Text('Company', size=(18, None), pad=(None, 8)), sg.InputText(key='companay', enable_events=True)],
            [sg.Text('First Name', size=(18, None), pad=(None, 8)), sg.InputText(key='fname', enable_events=True)],
            [sg.Text('Last Name', size=(18, None), pad=(None, 8)), sg.InputText(key='lname', enable_events=True)],
            [sg.Button('Previous', key='btn_prev', pad=(None, 8)), sg.Button('Next', key=('btn_next'))]]

def validateInput(input):
    if re.match("[\w.]+@[\a-zA-z]+(\.[a-z]+)+$", input['email']):
        print('email')
    if re.match(".{8,}", input['pass']):
        if input['pass'] == input['repass']:
            print('password')
    

# layout =   []
# row = []

# sg.change_look_and_feel('Topanga')
# row += [sg.Frame('Sign Up', signupLayout())]
# layout += [row]
# window = sg.Window('Login', layout)

# while True:
#     event, values = window.Read()
#     if event is None:
#         break
#     if event == 'btn_next':
#         validateInput(values)
    # else:
    #     if(event == 'username'):
    #     elif(event == 'pass')


# lst = ['item', 'test', 'office2012', 'test1', 'liscense', 'key']

# if any('office2013' in item for item in lst):
#     print('pass')

import sys
import tty
tty.setcbreak(sys.stdin)

while True:
    print ord(sys.stdin.read(1))
PI = 3.14
PI=2
print(PI)
=======
import subprocess as sp
import string
p=sp.run('echo 1 | sudo -S echo 1', shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
print(p.stderr)
print(p.stdout)
>>>>>>> origin/hoi
