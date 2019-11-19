import CreateVMsGui as gui1
import ConfigVMsGui as gui2

def createGui(i, scr):   
    if i == 0:
        return gui1.Gui1()

    elif i == 1:
        return gui2.Gui2(scr)
    else:
        return None

