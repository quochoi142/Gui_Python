import gui_Factory as fac
import extensions as etx

scr = []
# lstVM = []
pos = 0
scr.append(fac.createGui(pos, scr))

while 1:
    additive = 0
    result =  scr[pos].listen()     #appear(scr[pos])
    # print(scr[0].Values)

    if result == 0:
        break
    elif result == 1:
        # the first screen is Special-> create VM
        if pos == 0:
            if pos + 1 < len(scr):
                scr[pos+1] = fac.createGui(pos + 1, scr)
          
            else:
                scr.append(fac.createGui(pos + 1, scr))
        # elif pos == 1:
        #     etx.install(scr)
        #     break
        # gen.config(scr)
        #     # print(scr[pos].lstApps)
        #     break
        # Others screen
        elif pos==2:
            break
        else:
            if pos + 1 < len(scr):
                scr[pos+1].getGui().UnHide()
            else:
                scr.append(fac.createGui(pos + 1, scr))
        scr[pos].getGui().Hide()
        additive = 1
    elif result == -1:
        scr[pos].getGui().Hide()
        scr[pos-1].getGui().UnHide()
        additive = -1
    pos += additive
    # print('end')

for element in scr:
    element.getGui().Close()
