import PySimpleGUI as sg


def createInstance():
    return  [sg.Text("Ram"),sg.Combo([1,2,3,4],default_value=1), sg.InputText(), sg.Text("CPU"),
         sg.InputText(), sg.Text("Hard_disk"), sg.InputText()]
        #[sg.Checkbox("a"), sg.Checkbox("a"), sg.Checkbox("a")]
    
def createApp():
    return [sg.Checkbox("a"), sg.Checkbox("a"), sg.Checkbox("a")]


temp = [
        [sg.Text("Ram"), sg.Combo([1,2,3,4],default_value=1), sg.Text("CPU"),
         sg.InputText(), sg.Text("Hard_disk"), sg.InputText()],
        [sg.Checkbox("a"), sg.Checkbox("a"), sg.Checkbox("a")],

        [sg.Text("Ram"), sg.InputText(), sg.Text("CPU"),
         sg.InputText(), sg.Text("Hard_disk"), sg.InputText()],
        [sg.Checkbox("a"), sg.Checkbox("a"), sg.Checkbox("a")],

        [sg.Text("Ram"), sg.InputText(), sg.Text("CPU"),
         sg.InputText(), sg.Text("Hard_disk"), sg.InputText()],
        [sg.Checkbox("a"), sg.Checkbox("a"), sg.Checkbox("a")]

    ]
instances = []
for i in range(0,4):
    instances.append(createInstance())
    instances.append(createApp())





window = sg.Window('SetInstant', instances)

event, values = window.Read()

window.Close()
