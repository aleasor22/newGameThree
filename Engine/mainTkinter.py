from PIL import ImageTk, Image
from tkinter import *
import tkinter as tk
import keyboard

class mainApplication():
	"""
	Parameters
	----------
	FPS
		int, how many times the canvas refreshes.
	Methods
	-------
	:ref:windowSetUp(self)
	:ref:closeWindow(self)
	OLD
	---
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
		self.__FPS = 1000 / 30
		self.__mainApp = tk.Tk() #Tkinter window
		self.__version = title
		self.__screenWidth = 1280
		self.__screenHeight = 768
		self.__render = None#Canvas(self.__mainApp, height=self.__screenHeight, width=self.__screenWidth, bg='Grey')
		self.__gridSpot = [] #a list where each index is a tuple of a cordinate spot. 

		#Entity setup
		# self.player = Player()

	def windowSetUp(self):
		"""
		Description
		-----------
		Creates the tkinter window and sets up the canvas inside that window.
		"""
		##Generates title and tk window size
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__screenWidth)+'x'+str(self.__screenHeight))

		#Packs the .__render into the tkinter window
		self.createCanvas()
		self.createGrid(visability=True)
		#Calls the main loop of the tkinter window
		self.__mainApp.mainloop()

	def closeWindow(self):
		"""Calls .quit() method to close the tkinter window."""
		self.__mainApp.quit()

	def createCanvas(self):
		"""Creates the canvas and pushes it to screen."""
		self.__render = Canvas(self.__mainApp, height=self.__screenHeight, width=self.__screenWidth, bg="Grey")
		self.__render.grid(row=0, column=0, )#rowspan=10)
		self.__render.grid_propagate(0)

		
		# self.__render.create_line(64, 64, 128, 64, activewidth=1000)
		# self.__render.create_line(64, 84, 128, 84)

		

	#default grid size to 32x32, 40x24 boxes  or 960 total boxes
	#default grid size of 64x64, 20x12 boxes  or 240 total boxes
	def createGrid(self, gridSize=64, visability=False):
		"""
		Method: createGrid
		req. Arguments:
			gridSize = int, default=64, declares how large or small each box of the grid will be. 
			visibility = boolean, default=False, determins if the grid space is visible in the tkinter window. 
		Description: Populates the .__gridSpot list with coordinates of the top left corner of each box as a tuple (x, y)
		Returns: None
		"""
		#finds out how many squares would exist per square size
		gridWidth = int(self.__screenWidth / gridSize)
		gridHeight = int(self.__screenHeight / gridSize)

		#grid starting coords
		x, y = (0, 0)

		for i in range(gridHeight):
			x = 0 #resets x to 0 after each loop of "j"
			for j in range(gridWidth):
				#sets (x, y) to first list spot
				self.__gridSpot.append((x, y))
				x += gridSize
			y += gridSize

		##If set to true then display lines that show the borders of each tile
		#Trying out rectangles instead of lines for grid. 
		if visability:
			print(gridWidth, gridHeight)
			posX, posY = (0, 0)
			for i in range(gridWidth):
				posY = 0 #reset to 0 after each loop of "j"
				for j in range(gridHeight):
					self.__render.create_rectangle(posX, posY, posX+gridSize, posY+gridSize, tags="VisualGrid")
					posY += gridSize
					# print((i, j))
				posX += gridSize				

			
		##Call get_gridSpot if you want the whole list

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
		
	##Setters
	def set_screenSize(self, width, height):
		"""Sets the height and width of the application."""
		self.__screenHeight = height
		self.__screenWidth = width

