import gui1
import gui2

def createGui(i, scr):   
    if i == 0:
        return gui1.create(scr)
    elif i == 1:
        return gui2.create(scr)
    else:
        return None

