import PySimpleGUI as sg
from IGui import IGui

# layout = [
#     [sg.Checkbox('Windows 7', default=True, key = 'win7', size=(15, 10)),
#      sg.Text('Numbers of VMs'),
#      sg.Spin([1, 2, 3, 4], initial_value = 1, key = 'win7_num')],
#     #  sg.Radio('Default', 'mode1', default=True, key = 'default_win7'), 
#     #  sg.Radio('Custom', 'mode1', key = 'custom_win7'))],
#     [sg.Checkbox('Windows 10', default=True, key = 'win10', size = (15, 10)), 
#      sg.Text('Numbers of VMs'),
#      sg.Spin([1, 2, 3, 4], enable_events = True ,initial_value = 1, key = 'win10_num')],
#     [sg.Checkbox('Windows Server', default=True,  key = 'ws', size=(15, 10)), 
#      sg.Text('Numbers of VMs'), 
#      sg.Spin([1, 2, 3, 4], initial_value = 1, key = 'ws_num')],
#     # [sg.Submit('Default', key = 'btn_default')],
#     [sg.Submit('Next', key = 'btn_next')]
# ]
#     # print(selectScripts)

# def create(scr):
#     window = sg.Window('Config', layout)
#     return window

# def destroy():
#     window.Close()

class CreateVMsGui(IGui):
    def __init__(self):
        #sp.call('./Install/Step1.sh')
        layout = [
            [sg.Checkbox('Windows 7', default=True, key = 'win7', size=(15, 10)),
            sg.Text('Numbers of VMs'),
            sg.Spin([1, 2, 3, 4], initial_value = 1, key = 'win7_num')],
            #  sg.Radio('Default', 'mode1', default=True, key = 'default_win7'), 
            #  sg.Radio('Custom', 'mode1', key = 'custom_win7'))],
            [sg.Checkbox('Windows 10', default=True, key = 'win10', size = (15, 10)), 
            sg.Text('Numbers of VMs'),
            sg.Spin([1, 2, 3, 4], enable_events = True, initial_value = 1, key = 'win10_num')],
            [sg.Checkbox('Windows Server', default=True,  key = 'ws', size=(15, 10)), 
            sg.Text('Numbers of VMs'), 
            sg.Spin([1, 2, 3, 4], initial_value = 1, key = 'ws_num')],
            # [sg.Submit('Default', key = 'btn_default')],
            [sg.Submit('Next', key = 'btn_next')]
        ]
        self.window = sg.Window('Config', layout)

    def getGui(self):
        return self.window

    def listen(self):
        while True:
            event, values = self.window.Read()
            self.Values = values
            if event is None:
                return 0
            elif event == 'btn_next':
                return 1
            elif event == 'btn_prev':
                return -1
       