import os
import psutil
import getInforScreen as genYaml
import generateConfig as gen

# def getAllTag():
#     arr = []
#     for file in os.listdir("/home/nguyenhung/.hatch/scripts"):
#         if file.endswith(".ps1"):
#             # print(file)     
#             arr.append(file.split(".ps1")[0])      
#     return arr

def getAllfile(path, tag):
    arr = []
    for file in os.listdir(path):
        if file.endswith(tag):
            # print(file)     
            arr.append(file.split(tag)[0])      
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


#get hostname
import socket
hostname = socket.gethostname()



#get home directory
import os
homedir = os.environ['HOME']



import netifaces as ni
def getIp():
    nets=ni.interfaces()
    nets.remove('lo')
    return ni.ifaddresses(nets[0])[ni.AF_INET][0]['addr']


<<<<<<< HEAD
print(getIp())
=======
import subprocess
def install(scr):
    subprocess.call("./Intall/Step1.sh")
    genYaml.config(scr)
    subprocess.call("./Intall/Step2.sh")
    #gen.configData()
    subprocess.call("./Intall/Step3.sh")
    #### Create account Postgres
    subprocess.call("./Intall/Step4.sh")







>>>>>>> origin/hoi


