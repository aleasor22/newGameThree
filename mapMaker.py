from GUI import *
import keyboard


newMap = GUI_Main()
newMap.launchWindow()


def guiLoop():
    newMap.loopWindow()

    if keyboard.is_pressed('w') == True:
        print("Howdy")
    # if keyboard.is_pressed('q') == True:
    #     newMap.closeWindow()
    if keyboard.is_pressed('q') == False:
        guiLoop()
    else:
        newMap.closeWindow()

    # newMap.get_tk().after(int(100/30), guiLoop())


guiLoop()
