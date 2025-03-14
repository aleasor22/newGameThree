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
		self.__mapFileLocation = './z_Maps'

		self.__isFileOpen = False		##Bool, True if an individual file is open
		self.__isProjectOpen = False	##Bool, True if a project file is open (FUTURE)
		self.__currentOpenFile = None

		##----FILE CHANGED LOGIC----##
		# self.lastChange = None ##UNUSED AS OF [v0.0.5]



		##----END OF INIT METHOD----##
	
	def newFile(self, txt=None):
		"""
		Required Arguments
		------------------
		|   - txt - *str* - the name of the new file to be created
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
			#		font=('calibre',10,'normal')
			txtBox = Entry(newWindow, width=40, )
			okButton = Button(newWindow, text="ok", width=10, height=1, command=lambda:self.newFile(txtBox))
			cancelButton = Button(newWindow, text="cancel", width=10, height=1, command=newWindow.destroy)

			##----RENDERING WIDGETS TO SCREEN----##
			txtBox.propagate(False)
			okButton.propagate(False)
			cancelButton.propagate(False)
			txtBox.grid(row=0, column=0, columnspan=5)
			okButton.grid(row=1, column=1)
			cancelButton.grid(row=1, column=3)

			##----DETERMINS WHERE THE WINDOW WILL BE PLACED----##111
			ws = self.__mainApp.winfo_width() # width of the screen
			hs = self.__mainApp.winfo_height() # height of the screen

			x = (ws/2) - (244/2)
			y = (hs/2) - (45/2)
			newWindow.geometry('%dx%d+%d+%d' % (244, 45, x, y))
			newWindow.mainloop()
		else:
			## MAKES A NEW TXT FILE AT THIS LOCATION, WITH THE NAME ENTERED TO THE ENTRY WIDGET
			location = self.__mapFileLocation+"\\"+txt.get()+".txt"
			newFile = open(location, 'x')
			# newFile.write("testing") ## Logic that actually writes to files here
			newFile.close()


	def openFile(self):
		"""Opens file to be processed by tkinter then displayed."""
		try:
			file = filedialog.askopenfile(title="Open File...", filetypes=self.__commonFileTypes, initialdir=self.__mapFileLocation)
			self.__isFileOpen = True
		
			file = open(str(file.name), 'w')
			self.__currentOpenFile = file.name
			try:
				file.write("Lor\/um Ipsum")
			except:
				print("Error Writing to file")
			finally:
				file.close()
				print("file closed")
		except:
			print("File didn't open")

    
	def saveFile(self, saveAs=True):
		"""
		Required Arguments
		------------------
		|   - saveAs - *bool* - Default True, determins if the file is saved.., or saved as..
		---
		Saves the "Game View" window to a txt file."""
		if saveAs:
			file = filedialog.asksaveasfilename(title="Save File As...", filetypes=self.__commonFileTypes, initialdir=self.__mapFileLocation)
		else:
			##--FILE WILL NEED TO BE A CLASS VARIABLE TO ALLOW SAVES FROM THE MENU DROP DOWN--#
			## EX. open(str(FILEOBJ.name), 'w')
			print("place holder")
			pass
		

	##----DETECTING FILE CHANGES----##
	def fileChangedMsg(self, filePath=None, interval=1):
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


	##----PULLS TEXT FROM ENTRY WIDGET----##
	def get_txtFromEntry(self, entryWidget):
		"""Prints to screen the text put into the 'entryWidget'"""
		print(entryWidget.get())

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

	
	##----SETTERS----##
	# def set_varName(self, newVar): ##EXAMPLE
	# 	"""Sets newVar to self.__varName"""
	# 	self.__varName = newVar