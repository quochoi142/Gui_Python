import os
import psutil

def getAllTag():
    arr = []
    for file in os.listdir("/home/hoivu/.hatch/scripts"):
        if file.endswith(".ps1"):       
            arr.append(file.split(".ps1")[0])
        
    return arr





print(psutil.cpu_count())
print(int(psutil.virtual_memory()[0]/(1000**3)))
print(round(psutil.disk_usage("/")[2]/(1000**3),1))


