##IMPORTS START HERE
from .windowNode import mainApplication
from .imageNode import iNode
from .filesNode import fNode
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import *
import keyboard
import re

##START OF EVENTS TKINTER CLASS
class evNode(iNode, fNode):
	"""
	Events Node
	==========
	Class Parameters
	----------------
	|   - mainApp - *protected - obj* - the Tkinter object where all game based objects are housed
	Class Description
	-----------------
		Where all the events that trigger in applications will be written. 
	"""
	def __init__(self, mainApp, RENDER, rootPath):
		iNode.__init__(self, canvas=RENDER)
		fNode.__init__(self, mainApp, rootPath)
		##----END OF INIT----##



	##----START OF COMMAND METHODS----##
	def printMsgToScreen(self):
		"""Prints a special message to screen"""
		print("**NO COMMAND YET**")

	def openShortCuts(self):
		"""Generates a new Tkinter window used to display all avaialable shortcuts to screen"""
		##New instance of windowNode
		window = mainApplication()
		window.newWindow(title="All Shortcuts", screenSize=(500, 300))
		# window.set_columnConfig()
		
		fileToRead = open(self._helpFileLocation + "/shortcuts.txt", 'r')
		
		posX = 0
		posY = 0
		for index in fileToRead.readlines():
			line = re.sub("::", "\t ", index)
			line = re.sub("\n", "", line)
			
			if re.search("\~", line):
				print("breakpoint")
				posX += 1
				posY = 0
				continue
			label = Label(window.get_mainApp(), text=line)
			label.grid(row=posY, column=posX, sticky="w")

			# label.propagate(False)

			posY += 1
		
		window.get_mainApp().mainloop()

	def openHelpScreen(self):
		pass
	##----END OF COMMAND METHODS----##

    
        