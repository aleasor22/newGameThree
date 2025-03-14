from Engine import *
import keyboard
import os

##Handels active events that need to be consistently tested for
def developmentLoop():
    #Kill switch
    if keyboard.is_pressed('q') == True:
        TKINTER.closeWindow()

    ##----START OF ACTIVE EVENTS----##
    if WIDGETS.get_isFileOpen():
        # print("A file is opened")
        WIDGETS.fileChangedMsg()

    ##----END OF ACTIVE EVENTS----##

    TKINTER.get_mainApp().after(int(TKINTER.get_FPS()), developmentLoop)
	##----END OF GAME LOOP----##


##Code that compiles once on the first run of the code
print('\n\n\n')
print('<<----------------------------->>')
print('<<-------Initial Set UP-------->>')
print('<<----------------------------->>')

##Root directory
ROOT = os.path.dirname(__file__)

##Title of the app (str)
TITLE = "Map Developer [v0.0.51]"

##----BEGINNING OF CLASS CALLS----##
##Creates a tkinter object
TKINTER = mainApplication(TITLE)
RENDER = TKINTER.get_render()
##Creates Widget Object
WIDGETS = wNode(TKINTER.get_mainApp(), RENDER, ROOT)

##----START OF INITIAL SETUP----##
WIDGETS.menusSetUp()
WIDGETS.buttonSetUp()


##----END OF INITIAL SETUP----##

##Tkinter Setup (Defaults to 1280 by 768)
# TKINTER.set_screenSize(1920, 1024) #stick with default for  now

##Code that runs repeatedly while the app is open.
print('\n<<-------Game Main Loop-------->>\n')
developmentLoop()


#This has to be after 'developmentLoop()
TKINTER.windowSetUp(visibility=True)

##Signifies the end of the program
print('\n\n\n')
print('<<----------------------------->>')
print('<<-------------END------------->>')
print('<<----------------------------->>')