##IMPORTS START HERE
from .windowNode import mainApplication
from pynput import mouse, keyboard
from .imageNode import iNode
from .filesNode import fNode
from tkinter import *
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
	def printMsgToScreen(self, widget):
		"""Prints a special message to screen"""
		print("**NO COMMAND YET**")
		widget.bell()

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


	##----START OF MOUSE ACTION METHODS----##
	# def mouseSetUp(self):
	# 	"""Where all the mouse methods get called"""
	# 	self.rightClick()
	# 	self.leftClick()
	# 	pass
	
	# def rightClick(self):
	# 	"""Logic to process when 'M2' is pressed"""
	# 	if mouse.is_pressed('right'):
	# 		print("M2 was/is pressed")
	# 		# self.printMsgToScreen()

	# 	# print("M2 Pressed")
	
	# def leftClick(self):
	# 	"""Logic to process when 'M1' is pressed"""
	# 	if mouse.is_pressed('left'):
	# 		print("M1 was/is pressed")
	# 		# self.printMsgToScreen()

	# def isMouseInWindow(self):
	# 	"""Returns True or False based on if the mouse is inside the tkinter window."""		
	# 	windowPos = (self.get_mainApp().winfo_x(), self.get_mainApp().winfo_y())

	# 	if mouse.get_position()[0] > self.get_mainApp().winfo_x() and mouse.get_position()[0] < (windowPos[0]+self.get_mainApp().winfo_width()):
	# 		if mouse.get_position()[1] > self.get_mainApp().winfo_y() and mouse.get_position()[1] < (windowPos[1]+self.get_mainApp().winfo_height()):
	# 			# print("within window")
	# 			return True
	# 		else:
	# 			# print("outside window")
	# 			return False
	# 	else:
	# 		# print("outside window")
	# 		return False
	##----END OF MOUSE ACTION METHODS----##

   	##----START OF KEYBOARD ACTION METHODS----##
	# def keyboardSetUp(self):
	# 	"""Where all the keyboard methods get called"""
	# 	pass
	
	##----END OF KEYBOARD ACTION METHODS----##  