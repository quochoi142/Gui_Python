import PySimpleGUI as sg


def createInstance():
    return  [sg.Text("Ram"), sg.InputText(), sg.Text("CPU"),
         sg.InputText(), sg.Text("Hard_disk"), sg.InputText()]
        #[sg.Checkbox("a"), sg.Checkbox("a"), sg.Checkbox("a")]
    
    


temp = [
        [sg.Text("Ram"), sg.InputText(), sg.Text("CPU"),
         sg.InputText(), sg.Text("Hard_disk"), sg.InputText()],
        [sg.Checkbox("a"), sg.Checkbox("a"), sg.Checkbox("a")],

        [sg.Text("Ram"), sg.InputText(), sg.Text("CPU"),
         sg.InputText(), sg.Text("Hard_disk"), sg.InputText()],
        [sg.Checkbox("a"), sg.Checkbox("a"), sg.Checkbox("a")],

        [sg.Text("Ram"), sg.InputText(), sg.Text("CPU"),
         sg.InputText(), sg.Text("Hard_disk"), sg.InputText()],
        [sg.Checkbox("a"), sg.Checkbox("a"), sg.Checkbox("a")]

    ]

Instance=[
   for i in range(0,4):
        createInstance()

]



window = sg.Window('SetInstant', isinstance)

event, values = window.Read()

window.Close()
