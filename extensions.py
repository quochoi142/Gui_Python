import os
import psutil

def getAllTag():
    arr = []
    for file in os.listdir("/home/nguyenhung/.hatch/scripts"):
        if file.endswith(".ps1"):
            # print(file)     
            arr.append(file.split(".ps1")[0])      
    return arr




def getRam():
    return int(psutil.virtual_memory()[0]/(1000**3))

def getCPU():
    return int(psutil.cpu_count())

def getDisk_Usage():
    return round(psutil.disk_usage("/")[2]/(1000**3),1)

#get username
import getpass
username = getpass.getuser()
print(username)

#get hostname
import socket
hostname = socket.gethostname()
print(hostname)

#get home directory
import os
homedir = os.environ['HOME']
print(homedir)



