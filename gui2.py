import PySimpleGUI as sg
import extensions as ext

def createInstance(name):
    return [sg.Text(text = name, font = '#ff3399', size=(10, 0)),
            sg.Text('Ram(Gb)'),
            sg.Slider(range = (4, ext.getRam()), default_value = 4,
                      orientation = 'horizontal', size=(10, 10), key = name + '_ram'),
            sg.Text('CPU'),
            sg.Combo(list(range(2, ext.getCPU() + 1)), default_value = 2, key = name + '_cpu'), 
            sg.Text('Hard_disk(Gb)'), 
            sg.InputText('256', size = (10, 30), key = name + '_memory'),
            sg.Combo([1, 2, 3, 4], default_value = 1, key = name + '_instance'), 
            sg.Button('Apps', key = name + '_btn_apps'),
            sg.Button('Reset', key = name + '_btn_reset')]
    #[sg.Checkbox('a'), sg.Checkbox('a'), sg.Checkbox('a')]

def createApp():
<<<<<<< HEAD
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
=======
    arr = []
    # return [sg.Checkbox(1), sg.Checkbox(2), sg.Checkbox(3)]
    for i in list(range(1, 31)):
        arr.append(sg.Checkbox(i))
    return arr


# instances = []
# for i in range(0, 4):
#     instances.append(createInstance())
#     # instances.append(createApp())

# instances.append([sg.Button('Previous', key='btn_prev'),
#                   sg.Button('Next', key=('btn_next'))])

class OS:
    os= ''
    num = 0

def create(scr):
    instances = []
    values = scr[0].Values
    arr = []
    lstOs =['win7','win10','ws']
    for os in lstOs:
        if values[os] is True:
            x = OS()
            x.os = os
            x.num = values[os + '_num']
            arr.append(x) 
    for i in arr:
        for j in range(1, i.num + 1):
            instances.append(createInstance(i.os + 'v' + str(j)))
        # instances.append(createApp())

    instances.append([sg.Button('Previous', key='btn_prev'),
                    sg.Button('Next', key=('btn_next'))])
    window = sg.Window('SetInstant', instances)
    return window

def destroy():
    window.Close()
>>>>>>> origin/dev
