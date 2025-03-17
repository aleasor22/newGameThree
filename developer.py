from pynput import keyboard, mouse
from Engine import *
import os

##Handels active events that need to be consistently tested for
def developmentLoop():
	##----START OF ACTIVE EVENTS----##
	if WIDGETS.get_isFileOpen():
		# print("A file is opened")
		WIDGETS.activeChanges()
	
	# print(INPUTS.x, INPUTS.y)

	##----END OF ACTIVE EVENTS----##

	MAINAPP.after(int(TKINTER.get_FPS()), developmentLoop)
	##----END OF GAME LOOP----##


##Code that compiles once on the first run of the code
print('\n\n\n')
print('<<----------------------------->>')
print('<<-------Initial Set UP-------->>')
print('<<----------------------------->>')

##Root directory
ROOT = os.path.dirname(__file__)

##Title of the app (str)
TITLE = "Map Developer [v0.0.53]"

##----BEGINNING OF CLASS CALLS----##
##Creates a tkinter object
TKINTER = mainApplication()
TKINTER.newWindow(title=TITLE, screenSize=(1920, 1080))
TKINTER.newCanvas(visibility=True, canvasSize=(1280, 768))
RENDER = TKINTER.get_render()
MAINAPP = TKINTER.get_mainApp()

##Creates Widget Object
WIDGETS = wNode(MAINAPP, RENDER, ROOT)

##Keyboard & Mouse Setup
INPUTS = inNode(MAINAPP, RENDER, WIDGETS)
INPUTS.bindAllEvents()

##----START OF INITIAL SETUP----##
WIDGETS.menusSetUp()
WIDGETS.buttonSetUp()

##----END OF INITIAL SETUP----##

##Code that runs repeatedly while the app is open.
print('\n<<-------Game Main Loop-------->>\n')
developmentLoop()


MAINAPP.mainloop() ##Must be called last - no matter what

##Signifies the end of the program
print('\n\n\n')
print('<<----------------------------->>')
print('<<-------------END------------->>')
print('<<----------------------------->>')