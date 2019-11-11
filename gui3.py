import os
import psutil
import PySimpleGUI as sg

def getAllTags(arr):
    for file in os.listdir("/home/nguyenhung/.hatch/scripts"):
        if file.endswith(".ps1"):
            # print(file)     
            arr.append(file.split(".ps1")[0])   

def checkBoxValue(tag):
    return [sg.Checkbox(f'{tag}', enable_events=True, key=f'{tag}', size=(15,10))] 

arrTag = []
getAllTags(arrTag)
print("---")
print(arrTag)
print(len(arrTag))
print("---")

col = [checkBoxValue(tag) for tag in arrTag]
layout = [[sg.Column(col, scrollable=True, vertical_scroll_only=True, justification="center")],
          [sg.Cancel('Exit')]]
window = sg.Window('test', layout, resizable=True)
selectScript = []

while True:
    event, values = window.Read()
    # print(event, "-----",  values, "\n")
    if event is None: 
        break
    if event == "Exit":
        break
    if event in selectScript:
        selectScript.remove(event)
    else:
        selectScript.append(event)

window.Close()

for key in selectScript:
    print(key)