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

layout = [checkBoxValue(tag) for tag in arrTag]
window = sg.Window('test', layout, size=(800,600), resizable=True)
window.Read()
window.Close()
