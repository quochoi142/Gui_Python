import os
import psutil
import PySimpleGUI as sg


def getAllTags(arr):
    for file in os.listdir("/home/nguyenhung/.hatch/scripts"):
        if file.endswith(".ps1"):
            # print(file)
            arr.append(file.split(".ps1")[0])

def checkBoxValue(tag, lstApps):
    if tag in lstApps:
        return [sg.Checkbox(f'{tag} ', default=True, enable_events=True, key=f'{tag}', size=(15, 10))]
    else:
        return [sg.Checkbox(f'{tag} ', enable_events=True, key=f'{tag}', size=(15, 10))]

def getApps(lstApps):
    col = [checkBoxValue(tag, lstApps) for tag in arrTag]
    layout = [[sg.Column(col, scrollable = True, vertical_scroll_only = True, justification = "center")],
              [sg.Button('Done', key='btn_done')]]
    window = sg.Window('test', layout, resizable = True)
    selectScripts = lstApps
    print(selectScripts)

    while True:
        event, values = window.Read()
        # print(event, "-----",  values, "\n")
        if event is None:
            break
        if event == "btn_done":
            break
        if event in selectScripts:
            selectScripts.remove(event)
        else:
            selectScripts.append(event)
    window.Close()
    # print(selectScripts)
    return selectScripts


arrTag = []
getAllTags(arrTag)

# print(len(arrTag))
# print("---")
# print(len(arrTag))
# print("---")

defaultScripts = [
    'schtasks', 'setres', 'windows', 'windows7', 'wallpaper-fetch', 'cppredist',
                'dotnet472', 'mscorsvw', 'schtasks', 'ps1logging', 'patchandgo', 'finalize'
]

for script in defaultScripts:
    if script in arrTag:
        arrTag.remove(script)

print(len(arrTag))
print("---")

