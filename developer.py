from Engine import *
import keyboard

def developmentLoop():
    #Kill switch
    print("hello, testOne")
    if keyboard.is_pressed('q') == True:
        TKINTER.closeWindow()


    TKINTER.get_mainApp().after(int(TKINTER.get_FPS()), developmentLoop)
	#end of gameLoop


print('\n\n\n')
print('<<----------------------------->>')
print('<<-------Initial Set UP-------->>')
print('<<----------------------------->>')
##Code that compiles once on the first run of the code
#Title of the app (str)
title = "Map Developer [v0.0.1]"
##Creates a tkinter object
TKINTER = mainApplication(title)


print('\n<<-------Game Main Loop-------->>\n')
##Code that runs repeatedly while the app is open.
developmentLoop()

#This has to be after 'developmentLoop()
#TKINTER.set_screenSize(64, 128)
TKINTER.windowSetUp()#True)


print('\n\n\n')
print('<<----------------------------->>')
print('<<-------------END------------->>')
print('<<----------------------------->>')