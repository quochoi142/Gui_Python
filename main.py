import gui_Factory as fac 


scr = []
def appear(win):
    while True:
        event, values= win.Read()
        win.Values=values
        if event is None:            
            return 0
        elif event=='btn_next':
            return 1
        elif event=='btn_prev':
            return -1
       
            

def disappear(win):
    win.Hide()


pos=0
scr.append(fac.createGui(pos,scr))

while 1:
    additive=0
    
    
    result=appear(scr[pos])
    print(scr[0].Values)
    if result == 0:
        break
    elif result==1:
        
        if pos+1 < len(scr):
            scr[pos+1].UnHide()
        else: 
            scr.append(fac.createGui(pos+1,scr))  
        scr[pos].Hide()   
        additive=1
    elif result==-1:  
        scr[pos].Hide()
        scr[pos-1].UnHide()   
        additive=-1

    pos+=additive
   

for element in scr:
    element.Close()

    


