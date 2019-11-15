import gui_Factory as fac 

def appear(win):
    while True:
        event, values = win.Read()
        win.Values = values
        if event is None:            
            return 0
        elif event == 'btn_next':
            return 1
        elif event == 'btn_prev':
            return -1
        elif event == 'btn_default':
            # win.FindElement('win' + ).Update(disabled = True)
            # win.FindElement('win10').Update(disabled = True)
            parent_keys = list(win.AllKeysDict.keys())
            for key in parent_keys:
                win.FindElement(key).Update(disabled=True)
            print(parent_keys)

       
def disappear(win):
    win.Hide()

scr = []
pos=0
scr.append(fac.createGui(pos, scr))

while 1:
    additive=0
    result = appear(scr[pos])
    # print(scr[0].Values)

    if result == 0:
        break
    elif result == 1:
        #the first screen is Special-> create VM
        if pos == 0:
            if pos+1 < len(scr):
                scr[pos+1] = fac.createGui(pos + 1, scr)
            else: 
                scr.append(fac.createGui(pos + 1, scr))  
        #Others screen
        else:
            if pos+1 < len(scr):
                scr[pos+1].UnHide()
            else: 
                scr.append(fac.createGui(pos + 1,scr))  
        scr[pos].Hide()   
        additive=1
    elif result == -1:  
        scr[pos].Hide()
        scr[pos-1].UnHide()   
        additive = -1

    pos+=additive
   

for element in scr:
    element.Close()