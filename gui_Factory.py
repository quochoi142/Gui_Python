import gui1
import gui2


def createGui(i):
    
    if i == 0:
        return gui1.create()
    elif i==1:
        return gui2.create()
    else: return None

