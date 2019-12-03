from pathlib import *
import subprocess
import netifaces as ni
import socket
import getpass
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
    return round(psutil.disk_usage("/")[2]/(1000**3), 1)


# get username
username = getpass.getuser()


# get hostname
hostname = socket.gethostname()


# get home directory
homedir = os.environ['HOME']


def getIp():
    nets = ni.interfaces()
    nets.remove('lo')
    return ni.ifaddresses(nets[0])[ni.AF_INET][0]['addr']


def install(scr):
    subprocess.call("./Intall/Step1.sh")
    genYaml.config(scr)
    subprocess.call("./Intall/Step2.sh")
    # gen.configData()
    subprocess.call("./Intall/Step3.sh")
    # Create account Postgres
    subprocess.call("./Intall/Step4.sh")

from pathlib import *
print(str(Path.home()))
def getUser():
    return str(Path.home()).split('/')[2]
