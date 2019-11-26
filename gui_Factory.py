import CreateVMsGui as gui1
import ConfigVMsGui as gui2
import CreateAccountGui as gui3
import ProgressBarGui as gui4

def createGui(i, scr):
    if i == 0:
        return gui1.CreateVMsGui()
    elif i == 1:
        return gui2.ConfigVMsGui(scr)
    elif i == 2: 
        return gui3.CreateAccountGui(scr)
    elif i == 3:
        return gui4.ProgressBarGui(scr)
    else:
        return None
