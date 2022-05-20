
import random
import PySimpleGUI as sg

layout = [
            [sg.Text("choose your dice type",font=25)],
            [sg.Button("1d6",key="1d6"),sg.InputText(default_text="1-6",key="v1")],
            [sg.Button("1d10",key="1d10"),sg.InputText(default_text="1-10",key="v2")],
            [sg.Button("1d100",key="1d100"),sg.InputText(default_text="1-100",key="v3")],
            [sg.Button("1d3",key="1d3"),sg.InputText(default_text="1-3",key="v4")],
            
            

]
window = sg.Window("diceApp",layout)

while True:
    event, value = window.read()
    if event == None:
        break
    if event == "1d6":
        print("1d6が選択されました")
        sg.Popup("ダイスロール!!")
        dice = random.randrange(1,6)
        sg.Popup("1d6は"+str(dice)+"が出ました")
    if event == "1d10":
        print("1d10が選択されました")
        sg.Popup("ダイスロール!!")
        dice = random.randrange(1,10)
        sg.Popup("1d10は"+str(dice)+"が出ました")
    if event == "1d100":
        print("1d100が選択されました")
        sg.Popup("ダイスロール!!")
        dice = random.randrange(1,100)
        sg.Popup("1d100は"+str(dice)+"が出ました")
        if dice >= 95:
            sg.Popup("*F U M B L E*")
        elif dice <= 5:
            sg.Popup("*C R I T I C A L*")
    if event == "1d3":
        print("1d3が選択されました")
        sg.Popup("ダイスロール!!")
        dice = random.randrange(1,3)
        sg.Popup("1d3は"+str(dice)+"が出ました")
window.close() 
