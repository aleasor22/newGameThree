from tkinter import filedialog
from tkinter import *
import tkinter
import time
import os
import re

class fNode():
	"""
	Files Node
	==========
	Class Parameters
	----------------
	|	- commonFileTypes - *Private - list:tupel* - holds commond file types
	|	- mapFileLocation - *Private - str* - location of the folder that houses all map files
	|	- rootDir - *Private - str* - the file path to the root directory (dir:\\PythonProjects\\newGameThree)
	|	- isFileOpen - *Private - bool* - Represents if an individual file is open
	|	- isProjectOpen - *Private - bool* - Represents if a project file is open (FUTURE)
	|	- currentOpenFile - *Private - obj* - the currently open file
	Class Description
	-----------------
		Where any manipulation of files is handled
	"""
	def __init__(self, mainApp, rootPath):
		##----START OF INIT METHOD----##

		##----DECLARATION OF FILE VARIABLES----##
		self.__mainApp = mainApp
		self.__rootDir = rootPath ## currently unused
		self.__commonFileTypes = [('Text Document', '*.txt'), ('All Files', '*.*')]
		self._mapFileLocation = './z_Maps'
		self._helpFileLocation = './z_Docs'

		self.__isFileOpen = False		##Bool, True if an individual file is open
		self.__isProjectOpen = False	##Bool, True if a project file is open (FUTURE)
		self.__currentOpenFile = None

		##----FILE CHANGED LOGIC----##
		# self.lastChange = None ##UNUSED AS OF [v0.0.5]

		##----CHECK IF PATHS EXIST----#
		# if os.path.exists(path=self.__helpFileLocation) == False:
		# 	os.mkdir(self.__helpFileLocation)



		##----END OF INIT METHOD----##
	
	def newFile(self, andOpen=False, txt=None):
		"""
		Required Arguments
		------------------
		|   - txt - *str* - the name of the new file to be created
		|   - andOpen - *bool* - if true, opens the newly created file. 
		Method Description
		------------------
			Creates a temporary window that will be used to enter a new name to a txt file. A new file can also be made using the Save As... method.
		"""
		if txt == None:
			##----CREATING NEW WINDOW----#
			newWindow = tkinter.Tk()
			newWindow.title("File Wizard")
			##DEFAULT SIZE (244, 45)
			newWindow.propagate(False)

			##----DECLARING WIDGETS----##
			#NOTE		font=('calibre',10,'normal')
			txtBox = Entry(newWindow, width=40, )
			createButton = Button(newWindow, text="create", width=10, height=1, command=lambda:self.newFile(txt=txtBox))
			createOpenButton = Button(newWindow, text="create & open", width=10, height=1, command=lambda:self.newFile(andOpen=True, txt=txtBox))
			cancelButton = Button(newWindow, text="cancel", width=10, height=1, command=newWindow.destroy)

			##----RENDERING WIDGETS TO SCREEN----##
			activeWidgets = [txtBox, createButton, createOpenButton, cancelButton]
			self.set_propagateFalse(activeWidgets)
			txtBox.grid(row=0, column=0, columnspan=4)
			createButton.grid(row=1, column=1)
			createOpenButton.grid(row=1, column=2)
			cancelButton.grid(row=1, column=3)

			##----DETERMINS WHERE THE WINDOW WILL BE PLACED----##111
			ws = self.__mainApp.winfo_width() # width of the screen
			hs = self.__mainApp.winfo_height() # height of the screen

			x = (ws/2) - (244/2)
			y = (hs/2) - (45/2)
			newWindow.geometry('%dx%d+%d+%d' % (240, 45, x, y))
			newWindow.mainloop()
		elif andOpen:
			## MAKES A NEW TXT FILE AT THIS LOCATION, WITH THE NAME ENTERED TO THE ENTRY WIDGET
			## THEN CALLS THE openFile METHODD TO THEN READ THE FILE AND DISPLAY ON TO SCREEN
			print("AAAANNNNNND OPPPEEEEEN")
			self.openFile(newFile=True, txt=txt)
		else:
			## MAKES A NEW TXT FILE AT THIS LOCATION, WITH THE NAME ENTERED TO THE ENTRY WIDGET
			## ONLY CREATE THE FILE, DOES NOTHING WITH IT AFTER
			location = self._mapFileLocation+"\\"+txt.get()+".txt"
			newFile = open(location, 'x')
			# newFile.write("testing") ## Logic that actually writes to files here
			newFile.close()
			

	def openFile(self, newFile=False, txt=None):
		"""Opens file to be processed by tkinter then displayed."""
		self.__isFileOpen = True ## Set to true when active. 
		try:
			#Determins if the file is new or already exists. 
			if newFile and txt != None: ## Used when create & open is called during the "new File" menu widget
				## creates the file at the location, then save what is displayed on screen to this newly created file.
				fileLocation = self._mapFileLocation+"\\"+txt.get()+".txt"
				file = open(fileLocation, 'x')	#creates file, then opens it for writing
				self.writeToFile(fileName=file.name) ##This method will read the data from the screen then write it to the file. 
			else: ## used when the menu widget says "open file"
				fileLocation = filedialog.askopenfile(title="Open File...", filetypes=self.__commonFileTypes, initialdir=self._mapFileLocation)
				file = open(str(fileLocation.name), 'r')
				self.readFromFile(fileName=file.name) ##This method will read the data from the text file and display it to screen
			
			self.__currentOpenFile = file #Sets the file opened here to the currentOpenFile data
			file.close() #Closes the file when done with it. **Shouldn't we keep the file open till commanded closed?
		except:
				print("None-Type: No file was selected")

    
	def saveFile(self, saveAs=True):
		"""
		Required Arguments
		------------------
		|   - saveAs - *bool* - Default True, determins if the file is saved.., or saved as..
		---
		Saves the "Game View" window to a txt file.\
		"""
		if saveAs:
			file = filedialog.asksaveasfilename(title="Save File As...", filetypes=self.__commonFileTypes, initialdir=self._mapFileLocation)
		else:
			##--FILE WILL NEED TO BE A CLASS VARIABLE TO ALLOW SAVES FROM THE MENU DROP DOWN--#
			## EX. open(str(FILEOBJ.name), 'w')
			print("place holder")
			pass

	##----CLOSES THE ACTIVE FILE----##	
	def closeFile(self):
		"""Closes the active file, brings up a confirmation window if there is unsaved changes."""
		if self.__isFileOpen:
			##LOGIC TO DETERMIN IF THE FILE WAS CHANGED
			print("file is open")
			self.__currentOpenFile.close()
			print("file was closed")
			self.__isFileOpen = False
		else:
			print("No actively open file")

	def closeProject(self):
		pass


	##----DETECTING FILE CHANGES----##
	def activeChanges(self, filePath=None, interval=1):
		"""
		Required Arguments
		------------------
		|   - filePath - *str* - The file that is being checked for changes.
		----
		While a file is open, checks to see if a change has been made then prints to screen.
		"""
		##Generate variables currentState & lastChange
		# if filePath == None:
		# 	currentState = os.path.getmtime(str(self.__currentOpenFile))
		# else:
		# 	currentState = os.path.getmtime(filePath)
		# if self.lastChange == None or self.lastChange != currentState:
		# 	self.lastChange = currentState ##makes lastChange equal to currentState to now test to see if a new change was made
		# 	print("file changed")


		#NOTE: will need logic to exit this loop when closing file. 
			#Use recursive to call this funtion, so that it can update in the background, rather than taking precident and stoping all other logic.
		# while True:
		# 	lastChange = os.path.getmtime(filePath)
		# 	if currentState != lastChange:
		# 		print("File has changed!")
		# 		lastChange = currentState
		# 	time.sleep(interval)

	##----WRITE DATA TO FILE----##
	def writeToFile(self, fileName=None, ):
		"""Writes text to a given file"""
		#NOTE: cutsom exception logic to safely exit if no fileName was given
	##----READS DATA FROM FILE----##
	def readFromFile(self, fileName=None):
		"""Reads text from a given file"""
		#NOTE: cutsom exception logic to safely exit if no fileName was given

	##----PULLS TEXT FROM ENTRY WIDGET----##
	def get_txtFromEntry(self, entryWidget):
		"""Prints to screen the text put into the 'entryWidget'"""
		print(entryWidget.get())
	

	##----ADDITIONAL PACKING METHODS----##
	def set_gridPropagateFalse(self, objectsToPropagate):
		"""
		Required Arguments
		------------------
		|   - objectsToPropagate - *list - obj* - List of objects to make grid_propagate(False)
		Method Description
		------------------
			Where specified Label Frame widgets have propagate settings changed to False.
		"""
		##----START OF METHOD----##
		for obj in objectsToPropagate:
			obj.grid_propagate(False)
		##----END OF METHOD----##
		
	def set_propagateFalse(self, objectsToPropagate):
		"""
		Required Arguments
		------------------
		|   - objectsToPropagate - *list - obj* - List of objects to make propagate(False)
		Method Description
		------------------
			Where specified Label Frame widgets have propagate settings changed to False.
		"""
		##----START OF METHOD----##
		for obj in objectsToPropagate:
			obj.propagate(False)
		##----END OF METHOD----##

	##----GETTERS----##
	# def get_varName(self): ##EXAMPLE
	# 	"""Returns variable self.__varName"""
	# 	return self.__varName

	def get_currentOpenFile(self):
		"""Returns the currently opened file"""
		return self.__currentOpenFile
	
	def get_isFileOpen(self):
		"""Returns bool of if a file is open"""
		return self.__isFileOpen

	def get_windowSize(self, window):
		print(window.winfo_width(), window.winfo_height())

	def get_mainApp(self):
		"""Returns variable self.__mainApp"""
		return self.__mainApp
	
	##----SETTERS----##
	# def set_varName(self, newVar): ##EXAMPLE
	# 	"""Sets newVar to self.__varName"""
	# 	self.__varName = newVar