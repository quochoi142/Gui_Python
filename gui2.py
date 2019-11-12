import PySimpleGUI as sg
import gui1 as prev

def createInstance():
    return  [sg.Text("Ram"),sg.Combo([1,2,3,4],default_value=1), sg.InputText(), sg.Text("CPU"),
         sg.InputText(), sg.Text("Hard_disk"), sg.InputText()]
        #[sg.Checkbox("a"), sg.Checkbox("a"), sg.Checkbox("a")]
    
def createApp():
    return [sg.Checkbox("a"), sg.Checkbox("a"), sg.Checkbox("a")]



instances = []
for i in range(0,4):
    instances.append(createInstance())
    instances.append(createApp())

instances.append([sg.Button("Previous", key='btn_prev'), sg.Button("Next", key=('btn_next'))])






def create():
    window = sg.Window('SetInstant', instances)
    return window


def destroy():
    window.Close()
