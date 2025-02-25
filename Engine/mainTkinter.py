from PIL import ImageTk, Image
from tkinter import *
import tkinter as tk
import keyboard

class mainApplication():
	"""
	mainApplication known as Main Application (runs tkinter for Game)
	Parent Class: None
	Class Variables:
		requires: title = str, holds what version number the game is in.
		private:
			.__FPS			= int, how many times the canvas refreshes.
			.__mainApp 		= obj, creates the tkinter window.
			.__version 		= str, what version the "game" is in. 
			.__screenWidth	= int, how manny pixels wide is the canvas.
			.__screenHeight	= int, how manny pixels tall is the canvas.
			.__render		= obj, the canvas object within tkinter
			.__gridSpot		= list, each index of the list houses a box of specific size 
		protected: None
		public: None
	Description: 
	"""
	#initialises class variables
	def __init__(self, title):
		#subject to change, so that it can be re-used for game.py and mapMaker.py
		self.__FPS = 1000 / 30
		self.__mainApp = tk.Tk() #Tkinter window
		self.__version = title
		self.__screenWidth = 1280
		self.__screenHeight = 768
		self.__render = Canvas(self.__mainApp, height=self.__screenHeight, width=self.__screenWidth, bg='Grey')
		self.__gridSpot = []

		#Entity setup
		# self.player = Player()

	def windowSetUp(self):
		"""
		Method: windowSetUp
		req. Arguments: None
		Description: Creates the tkinter window and sets up the canvas inside that window.
		Returns: None
		"""
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__screenWidth)+'x'+str(self.__screenHeight))
		self.createCanvas()
		# self.entitySetUp()
		self.__mainApp.mainloop()

	#background controlls
	def windowLoop(self):
		"""
		Method: windowLoop
		req. Arguments: None
		Description: Kills tkinter window when 'q' is pressed, refreshes screen after .__FPS time passes. (currently unused)
		Returns: None
		"""
		if keyboard.is_pressed('q') == True:
			self.closeWindow()
		self.__mainApp.after(int(self.__FPS), self.windowLoop)

	def closeWindow(self):
		"""Calls .quit() method to close the tkinter window."""
		self.__mainApp.quit()

	def createCanvas(self):
		"""Creates the canvas and pushes it to screen."""
		self.__render.grid(row=0, column=0, )#rowspan=10)
		self.__render.grid_propagate(0)

	#default grid size to 32x32, 40x24 boxes  or 960 total boxes
	#default grid size of 64x64, 20x12 boxes  or 240 total boxes
	def createGrid(self, gridSize=64):
		"""
		Method: createGrid
		req. Arguments:
			gridSize int, default=64, declares how large or small each box of the grid will be. 
		Description: Populates the .__gridSpot list with coordinates of the top left corner of each box as a tuple (x, y)
		Returns: None
		"""
		#finds out how many squares would exist per square size
		gridWidth = int(self.__screenWidth / gridSize)
		gridHeight = int(self.__screenHeight / gridSize)

		#grid starting coords
		x, y = (0, 0)

		for i in range(gridHeight):
			x = 0 #resets x to 0 after each loop of "i"
			for j in range(gridWidth):
				#sets (x, y) to first list spot
				self.__gridSpot.append((x, y))
				x += gridSize
			y += gridSize

	##Getters
	def get_screenSize(self):
		"""Returns screen size as a tuple, (width, height)"""
		return (self.__screenWidth, self.__screenHeight)

	def get_mainApp(self):
		"""Returns self.__mainApp"""
		return self.__mainApp

	def get_render(self):
		"""Returns self.__render"""
		return self.__render

	def get_FPS(self):
		"""Returns self.__FPS"""
		return self.__FPS

	def get_gridSpot(self, index=None):
		"""
		Argument: index = int, a specific index of the __gridSpot list
		Returns either self.__gridSpot or self.__gridSpot @ a given index."""
		# print(len(self.__gridSpot))
		if index == None:
			return self.__gridSpot
		else:
			return self.__gridSpot[index]
