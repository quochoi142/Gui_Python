import PySimpleGUI as sg
from IGui import IGui
class ProgressBarGui(IGui):
    def __init__(self):
        layout=[
            [sg.ProgressBar(max_value=100, orientation='horizontal',size=(20,20),
             key='progressbar')]
        ]
        self.window=sg.Window('Progress',layout)
    
    def getGui(self):
        return self.window
    

    def listen(self):
        i=0
        signal=1
        while 1:
            if i==100:
                signal=-1
            elif i==1:
                signal=1
            events, values = self.window.Read(timeout=10)
            i+=signal
            self.window['progressbar'].UpdateBar(i)
            if events is None:
              break
        self.window.Close()
