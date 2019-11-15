import gui_Factory as fac
import getInforScreen as gen
import getCheckedApp as app


def appear(win, lstApp):
    while True:
        event, values = win.Read()
        win.Values = values
        print(values)
        if event is not None:
            key = event.split('_')[0]
        # print(key)
        if event is None:
            return 0
        elif event == 'btn_next':
            return 1
        elif event == 'btn_prev':
            return -1
        elif 'btn_apps' in event:
            if key in lstApps.keys():
                lstApps[key] = app.getApps(lstApps[key])
            else:
                lstApps[key] = app.getApps([])
            scr[1].lstApps = lstApps
            print(lstApps)
        elif 'btn_reset' in event:
            print('reset')
            # disable btn
            # lstKeys = list(win.AllKeysDict.keys())
            # for key in lstKeys:
            #     if key in defaultBtnKeys or any(btnKey in key for btnKey in defaultBtnKeys):
            #         lstKeys.remove(key)
            #     else:
            #         win.FindElement(key).Update(disabled=True)
            # print(lstKeys)
            lstValues = ['memory', 'cpu', 'disk', 'instance']
            for value in lstValues:
                if value in defaultValues.keys():
                    win.FindElement(
                        key + '_' + value).Update(value=defaultValues[value])
                    print(lstApps)
            del lstApps[key]


def disappear(win):
    win.Hide()


defaultBtnKeys = ['btn_next', 'btn_prev', 'btn_exit', 'btn_reset', 'btn_apps']
defaultValues = {
    'memory': 2,
    'cpu': 2,
    'disk': 256,
    'instance': 1
}

scr = []
# lstVM = []
pos = 0
scr.append(fac.createGui(pos, scr))

while 1:
    lstApps = {}
    additive = 0
    result = appear(scr[pos], lstApps)
    # print(scr[0].Values)

    if result == 0:
        break
    elif result == 1:
        # the first screen is Special-> create VM
        if pos == 0:
            if pos+1 < len(scr):
                scr[pos+1] = fac.createGui(pos + 1, scr)
            else:
                scr.append(fac.createGui(pos + 1, scr))
        elif pos == 1:
            gen.config(scr)
            print(scr[pos].lstApps)
            break
        # Others screen
        else:
            if pos + 1 < len(scr):
                scr[pos+1].UnHide()
            else:
                scr.append(fac.createGui(pos + 1, scr))
        scr[pos].Hide()
        additive = 1
    elif result == -1:
        scr[pos].Hide()
        scr[pos-1].UnHide()
        additive = -1
    pos += additive

for element in scr:
    element.Close()
