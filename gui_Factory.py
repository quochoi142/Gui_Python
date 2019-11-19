import CreateVMsGui as gui1
import ConfigVMsGui as gui2


def createGui(i, scr):   
    if i == 0:
        return gui1.CreateVMsGui()

    elif i == 1:
        return gui2.ConfigVMsGui(scr)
   
    else:
        return None

