from Engine import *
import keyboard

def developmentLoop():
    #Kill switch
    #This works now
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
title = "Map Developer [v0.0.2]"
##Creates a tkinter object
TKINTER = mainApplication(title)

##Tkinter Setup (Defaults to 1280 by 768)
# TKINTER.set_screenSize(1920, 1024) #stick with default for  now

print('\n<<-------Game Main Loop-------->>\n')
##Code that runs repeatedly while the app is open.
developmentLoop()


#This has to be after 'developmentLoop()
TKINTER.windowSetUp(visibility=True)


print('\n\n\n')
print('<<----------------------------->>')
print('<<-------------END------------->>')
print('<<----------------------------->>')