##IMPORTS START HERE
from .windowNode import mainApplication
from pynput import mouse, keyboard
from .filesNode import fNode
from tkinter import *
import re

##START OF EVENTS TKINTER CLASS
class evNode(fNode):
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
	def __init__(self, mainApp, rootPath, canvas):
		## Inheritance calls
		fNode.__init__(self, mainApp=mainApp, rootPath=rootPath, canvas=canvas)
		
		
		##----START OF ACTIVE EVENT VARIABLES----##
		self.__isInRender = False ##Returns true when mouse is inside the Main Canvas
		self.__activeTask = None ##Returns ture if a menu widget is active
		##----END OF ACTIVE EVENT VARIABLES----##

		##----END OF INIT----##



	##----START OF COMMAND METHODS----##
	def printMsgToScreen(self, widget=None, optionalTxt='blank'):
		"""Prints a special message to screen"""
		print("**COMMAND {0} INACTIVE**".format(optionalTxt))
		if widget != None:
			print(widget.winfo_width(), widget.winfo_height())
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

	##----START OF MOUSE----#
	def inRender(self, event):
		self.__isInRender = True
		# print("Entered render at", (event.x, event.y))
		
	def outRender(self, event):
		self.__isInRender = False
		# print("Left Render at", (event.x, event.y))

	def positionInRender(self, event):
		if self.__isInRender:
			# print(event.x, event.y)
			self.local_x = event.x
			self.local_y = event.y
		
	def onM2Press(self, event):
		print(self.__activeTask, "Active Task")
		if self.__activeTask == None:
			self.widget.get_editMenuList().post(event.x_root, event.y_root) ##Calls the menu widget to produce to screen
		elif self.__activeTask == "placeImage":
			print("ENTER LOGIC TO DELETE MAP TILE WHEN 'placeImage' IS ACTIVE TASK")
		else:
			print("EVENT", self.__activeTask, "HAS NO M2 EVENT")
	
	def onM1Press(self, event):
		print(self.__activeTask, "Active Task")
		if self.__activeTask == None:
			print("DEFAULT M1 EVENT")
		elif self.__activeTask == "placeImage":
			print("IMAGE PLACEMENT EVENT")
		else:
			print("EVENT", self.__activeTask, "HAS NO M1 EVENT")

	def mouseScroll(self, event):
		print(self.__activeTask, "Active Task")
		if self.__activeTask == None:
			print("DEFAULT SCROLL EVENT")
	
	def onM3Press(self, event):
		print(self.__activeTask, "Active Task")
		if self.__activeTask == None:
			print("DEFAULT M3 EVENT")
		
	##----END OF MOUSE----#


	