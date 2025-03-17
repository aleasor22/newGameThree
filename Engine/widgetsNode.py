##IMPORTS START HERE
from .eventsNode import evNode
from PIL import ImageTk, Image
from tkinter import *
import tkinter as tk
import keyboard

##CLASS WIDGETS TKINTER STARTS HERE
class wNode(evNode):
	"""
	Widget Node
	==========
	Class Parameters
	----------------
	|	- mainMenu - *private - obj* - the Tkinter display view where every widget it housed
	|	- viewMenuList - *protected - obj* - Drop down group for "view"
	|	- futureMenuList - *protected - obj* - Drop down group for "Future"
	|	- fileMenuList - *protected - obj* - Drop down group for "File"
	|	- editMenuList - *protected - obj* - Drop down group for "Edit"
	|	- tilesList - *protected - obj* - Drop down group for "Tile"
	Class Description
	-----------------
		Where all sorts of widgets will be housed. Ex. Buttons, Lable Frames, drop down menus, etc...
	"""
	def __init__(self, mainApp, RENDER, rootPath):
		evNode.__init__(self, mainApp, RENDER, rootPath)

		##----DECLARATION OF MENUES----##
		self.__mainMenu			= Menu(mainApp) ##PARENT MENU OBJECT
		self._futureMenuList	= Menu(self.__mainMenu, tearoff=False)  #Placeholder for future menus
		self._tilesMenuList		= Menu(self.__mainMenu, tearoff=False)  #TBD what it does
		self._viewMenuList		= Menu(self.__mainMenu, tearoff=False)  #TBD what is does
		self._fileMenuList		= Menu(self.__mainMenu, tearoff=False)  #Common File Operations
		self._editMenuList		= Menu(self.__mainMenu, tearoff=False)  #Common Edit Operations
		self._helpMenuList		= Menu(self.__mainMenu, tearoff=False)  #Opens additional documentation for assistance (displays shortcuts)
		##----PACKS & PUSHES THE MENUS TO SCREEN----##
		mainApp.config(menu=self.__mainMenu)

		##----DECLARATION OF BUTTONS----## #NOTE IF NEEDED
		##----DECLARATION OF LABEL FRAMES----## #NOTE IF NEEDED
		##----END OF INIT----##

	##----DROP DOWN LOGIC----##
	def menusSetUp(self):
		"""Where all the Drop Down menus will be set up and packed to screen"""
		##----START OF METHOD----##

		## Call menu methods in order left to right
		self.fileMenu() #First
		self.editMenu()
		self.viewMenu()
		self.tilesMenus() #Last
		self.helpMenu() ##Will become the Help tab

		# self.compileMenuWidgets() ##Is this line needed?
		##----END OF METHOD----##
		pass

	##----START OF BUTTON LOGIC----##
	def buttonSetUp(self):
		"""Where all the buttons shown on the application will get called and packed to screen        """
		#NOTE#----CHANGES WILL BE MADE DURING PHASE C OF JOB[001]----##
		##----START OF METHOD----##
		##Creating Label Frames
		frameOne = LabelFrame(self.get_mainApp(), text="TEST-FRAME1", width=250, height=500, bg='Grey')
		frameTwo = LabelFrame(self.get_mainApp(), text="TEST-FRAME2", width=250, height=500, bg='Grey')
		##Creating Buttons
		TEST =  Button(self.get_mainApp(), text="TestOne", )
		TEST2 =  Button(frameOne, text="TestTwo", command=lambda:self.printMsgToScreen(TEST2))
		TEST3 =  Button(frameTwo, text="TestThree", )
		TEST4 =  Button(frameOne, text="TestFour", )

		##Packs every widget to screen
		#RENDER is at grid(row=0, column=0, rowspan=1280, columnspan=768)
		frameOne.grid(row=0, column=769, rowspan=500)
		self.set_gridPropagateFalse([frameOne, ])
		TEST2.grid(row=0, column=0)
		TEST4.grid(row=0, column=1)
		TEST3.grid(row=1, column=1)
		
		##----END OF METHOD----##

	##----LABEL FRAME GROUPS----#
	def labelFrameSetUp(self):
		"""Calls all methods that deal with Label Frames (FUTURE)"""
		##NOTE: Will be developed during phase C of JOB[001]
		pass

	##----END OF BUTTON LOGIC----##

	##----START OF MENU WIDGET LOGIC----##
	def futureMenus(self):
		"""Houses all the logic to goes into the "Future" drop down menu."""
		##----PLACEHOLDER DROPDOWNS----##
		self.__mainMenu.add_cascade(label="*FUTURE MENU*", menu=self._futureMenuList) ## Adds fileMenuList to main=Menu widget. 

		##----START OF COMMAND LOGIC---##
		self._futureMenuList.add_command(label="*FUTURE OPTION*", command=self.printMsgToScreen)
		self._futureMenuList.add_separator() #Spaces command options in a menu tab.
		self._futureMenuList.add_command(label="*FUTURE OPTION*", command=self.printMsgToScreen)
		##----END OF COMMAND LOGIC---##
	
	def fileMenu(self):
		"""Houses all the logic to goes into the "File" drop down menu."""
		##----FILE LOGIC----#
		self.__mainMenu.add_cascade(label="File", menu=self._fileMenuList) ## Adds fileMenuList to main=Menu widget. 

		##----START OF COMMAND LOGIC---##
		self._fileMenuList.add_command(label="New File..", command=self.newFile)
		self._fileMenuList.add_command(label="Open..", command=self.openFile)
		self._fileMenuList.add_command(label="Save..", command=lambda:self.saveFile(saveAs=False))
		self._fileMenuList.add_command(label="Save as..", command=self.saveFile)
		self._fileMenuList.add_command(label="Close File", command=self.closeFile)
		self._fileMenuList.add_separator() #Spaces command options in a menu tab.
		self._fileMenuList.add_command(label="New Project..", command=self.printMsgToScreen)    ##NOTE FUTURE
		self._fileMenuList.add_command(label="Open Project..", command=self.printMsgToScreen)   ##NOTE FUTURE
		self._fileMenuList.add_command(label="Save Project..", command=self.printMsgToScreen)   ##NOTE FUTURE
		self._fileMenuList.add_command(label="Save Project as..", command=self.printMsgToScreen)##NOTE FUTURE
		self._fileMenuList.add_command(label="Close Project", command=self.closeProject)		##NOTE FUTURE
		self._fileMenuList.add_separator() #Spaces command options in a menu tab.
		self._fileMenuList.add_command(label="Exit", command=self.get_mainApp().quit)
		##----END OF COMMAND LOGIC---##
         
    
	def editMenu(self, rightClick=False, pos=(0, 0)):
		"""
		Method Description
		------------------
			Houses all the logic to goes into the "Edit" drop down menu.
		"""
		##----EDIT LOGIC----#
		self.__mainMenu.add_cascade(label="Edit", menu=self._editMenuList) ## Adds fileMenuList to main=Menu widget. 

		##----START OF COMMAND LOGIC---##
		self._editMenuList.add_command(label="UNDO	ctrl+z", command=self.printMsgToScreen)
		self._editMenuList.add_command(label="REDO	ctrl+y", command=self.printMsgToScreen)
		self._editMenuList.add_separator() #Spaces command options in a menu tab.
		self._editMenuList.add_command(label="CUT   ctrl+x", command=self.printMsgToScreen)
		self._editMenuList.add_command(label="COPY  ctrl+c", command=self.printMsgToScreen)
		self._editMenuList.add_command(label="PASTE ctrl+v", command=self.printMsgToScreen)
		##----END OF COMMAND LOGIC---##

	def viewMenu(self):
		"""
		Method Description
		------------------
			Houses all the logic to goes into the "view" drop down menu.
		"""
		##----view LOGIC----##
		self.__mainMenu.add_cascade(label="View", menu=self._viewMenuList) ## Adds fileMenuList to main=Menu widget. 

		##----START OF COMMAND LOGIC---##
		self._viewMenuList.add_command(label="TBD", command=self.printMsgToScreen)
		##----END OF COMMAND LOGIC---##

	def tilesMenus(self):
		"""
		Method Description
		------------------
			Houses all the logic to goes into the "Tile" drop down menu.
		"""
		##----PLACEHOLDER DROPDOWNS----##
		self.__mainMenu.add_cascade(label="Tiles", menu=self._tilesMenuList) ## Adds fileMenuList to main=Menu widget. 

		##----START OF COMMAND LOGIC---##
		self._tilesMenuList.add_command(label="TBD", command=self.printMsgToScreen)
		self._tilesMenuList.add_separator() #Spaces command options in a menu tab.
		self._tilesMenuList.add_command(label="TBD", command=self.printMsgToScreen)
		##----END OF COMMAND LOGIC---##

	def helpMenu(self):
		"""
		Method Description
		------------------
			Houses all the logic to goes into the "Help" drop down menu.
		"""
		##----PLACEHOLDER DROPDOWNS----##
		self.__mainMenu.add_cascade(label="Help", menu=self._helpMenuList) ## Adds fileMenuList to main=Menu widget. 

		##----START OF COMMAND LOGIC---##
		self._helpMenuList.add_command(label="All Shortcuts", command=self.openShortCuts)
		self._helpMenuList.add_separator() #Spaces command options in a menu tab.
		self._helpMenuList.add_command(label="Help", command=self.printMsgToScreen)

	##----END OF MENU WIDGET LOGIC----##




	##----START OF GETTERS----##
	def get_buttonSize(self, buttonObject):
		"""Returns (width, length) of the button once it has been displayed to screen"""
		return (buttonObject.winfo_width(), buttonObject.winfo_height())
	
	def get_editMenuList(self):
		return self._editMenuList