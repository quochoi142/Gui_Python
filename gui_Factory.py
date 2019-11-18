import gui1
import gui2

def createGui(i, scr):   
    if i == 0:
        return gui1.Gui1()

    elif i == 1:
        return gui2.Gui2(scr)
    else:
        return None

