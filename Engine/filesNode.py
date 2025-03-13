from tkinter import filedialog
from tkinter import *
import time
import os
import re

class fNode():
	"""
	Files Node
	==========
	Class Parameters
	----------------
	|   - commonFileTypes - *Private - list:tupel* - holds commond file types
	|   - mapFileLocation - *Private - str* - location of the folder that houses all map files
	Class Description
	-----------------
		Where any manipulation of files is handled
	"""
	def __init__(self):
		##----START OF INIT METHOD----##

		##----DECLARATION OF FILE VARIABLES----##
		self.__commonFileTypes = [('Text Document', '*.txt'), ('All Files', '*.*')]
		self.__mapFileLocation = './z_Maps'



		##----END OF INIT METHOD----##


	def openFile(self):
		"""Opens file to be processed by tkinter then displayed."""
		file = filedialog.askopenfile(title="Open File...", filetypes=self.__commonFileTypes, initialdir=self.__mapFileLocation)
		open(str(file.name), 'r')
		# self.fileChangedMsg(file.name)
		file.close()
		pass
    
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
	def fileChangedMsg(self, filePath, interval=1):
		"""
		Required Arguments
		------------------
		|   - filePath - *str* - The file that is being checked for changes.
		----
		While a file is open, checks to see if a change has been made then prints to screen.
		"""
		##Generate variables currentState & lastChange
		lastChange = os.path.getmtime(filePath)
		currentState = lastChange ##makes lastChange equal to currentState to now test to see if a new change was made

		#NOTE: will need logic to exit this loop when closing file. 
			#Use recursive to call this funtion, so that it can update in the background, rather than taking precident and stoping all other logic.
		while True:
			lastChange = os.path.getmtime(filePath)
			if currentState != lastChange:
				print("File has changed!")
				lastChange = currentState
			time.sleep(interval)