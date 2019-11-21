import PySimpleGUI as sg
from IGui import IGui

class LicenseGui(IGui):
    def __init__(self, lstLicenses):
        print('license gui:', )
        layout = [[sg.Text("Please fill in License key software")]]
        row = []
        for machine in lstLicenses:
            print(machine)
            row = [
                [sg.Text(machine)],
                [
                    sg.InputText("", size=(50, 10),key='key')
                ]
            ]
            layout += row
            row = []
        layout += [[sg.Button("Done", key="btn_done")]]
        # print(layout)
        self.window = sg.Window('Lisence key', layout)

    def getGui(self):
        return self.window

    def listen(self):
        while True:
            event, values = self.window.Read()
            self.Values = values
            if event is None:
                return 0
            elif event == 'btn_done':
                if values['key'] == "":
                    return 0
                else:
                    return 1


# win = LicenseGui()
# if win.listen() == 0:
#     win.getGui().Close()
