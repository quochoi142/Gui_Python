import gui_Factory as fac
import extensions as etx
#import getCheckedApp as app

# def appear(win):
#     while True:
#         event, values = win.getGui().Read()
#         win.Values = values
#         lstApps=win.lstApps
#         # print(values)
#         if event is not None:
#             key = event.split('_')[0]
#         # print(key)
#         if event is None:
#             return 0
#         elif event == 'btn_next':
#             return 1
#         elif event == 'btn_prev':
#             return -1
#         elif 'btn_apps' in event:
#             if key in lstApps.keys():
#                 lstApps[key] = app.getApps(lstApps[key])
#             else:
#                 lstApps[key] = app.getApps([])
#             win.lstApps = lstApps
#         elif 'btn_reset' in event:
#             lstValues = ['memory', 'cpu', 'disk', 'instance']
#             for value in lstValues:
#                 if value in defaultValues.keys():
#                     win.getGui().FindElement(
#                         key + '_' + value).Update(value = defaultValues[value])
#             del lstApps[key]

# def disappear(win):
#     win.Hide()

# defaultBtnKeys = ['btn_next', 'btn_prev', 'btn_exit', 'btn_reset', 'btn_apps']
# defaultValues = {
#     'memory': 2,
#     'cpu': 2,
#     'disk': 256,
#     'instance': 1
# }

scr = []
# lstVM = []
pos = 0
scr.append(fac.createGui(pos, scr))

while 1:

    
    additive = 0
    result =  scr[pos].listen()#appear(scr[pos])
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
            #gen.config(scr)
        #     # print(scr[pos].lstApps)
        #     break
        # Others screen
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
