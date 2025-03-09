from PIL import ImageTk, Image
from tkinter import *
import tkinter as tk
import keyboard

class mainApplication():
	"""
	Main Application
	================
	Class Parameters
	----------------
	|   - FPS - *private - int* - Screens refresh rate interval.
	|   - mainApp - *private - obj* - creates the tkinter window.
	|   - version - *private - str* - The version of the application.
	|	- screenWidth - *private - int* - How manny pixels wide is the canvas.
	|	- screenheight - *private - int* - How manny pixels tall is the canvas.
	|	- render - *private - obj* - Tkinter's canvas object.
	|	- gridSpot - *private - list* Each index of the list houses a box on the canvas like a coordinate plane. 
	| 
	Class Description
	-----------
		Custom interface with tkinter. Anything that is done through tkinter is housed here with a few exceptions. Exception Ex: Image Node
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

	def windowSetUp(self, visibility=False):
		"""
		Required Arguments
		------------------
		|   - visibility - *bool* - Determins if a grid will be visabily shown on screen
		Method Description
		------------------
			Creates the tkinter window and sets up the canvas inside that window.
		"""
		##Generates title and tk window size
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__screenWidth)+'x'+str(self.__screenHeight))

		#sets the new canvas to self.__render, then packs the canvas to screen
		self.__render = Canvas(self.__mainApp, height=self.__screenHeight, width=self.__screenWidth, bg="Grey")
		self.__render.grid(row=0, column=0, )#rowspan=10)
		self.__render.grid_propagate(0)

		#creates the grid that is applied in the background to the canvas, Optional visibility of the grid. 
		self.createGrid(shown=visibility)

		#Calls the main loop of the tkinter window
		self.__mainApp.mainloop()

	def closeWindow(self):
		"""Calls tkinter's .quit() method to close the tkinter window."""
		self.__mainApp.quit()


	#default grid size to 32x32, 40x24 boxes  or 960 total boxes
	#default grid size of 64x64, 20x12 boxes  or 240 total boxes
	def createGrid(self, gridSize=64, shown=False):
		"""
		Required Arguments
		------------------
		|   - gridSize - *int* - The size of each box within the grid.
		|   - shown - *bool* - Determins if the grid layout will be visible or not
		Method Description
		------------------
			Populates the gridSpot list with coordinates of the top left corner of each grid box as a tuple (x, y)
		"""
		#finds out how many squares would exist per square size
		gridWidth = int(self.__screenWidth / gridSize) #width(1280)/gridSize(64) = gridWidth(20)
		gridHeight = int(self.__screenHeight / gridSize) #height(768)/gridSize(64) = girdHeight(12)

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
		if shown:
			# print(gridWidth, gridHeight)
			posX, posY = (0, 0)
			for i in range(gridHeight):
				posX = 0 #reset to 0 after each loop of "j"
				for j in range(gridWidth):
					self.__render.create_rectangle(posX, posY, posX+gridSize, posY+gridSize, tags="VisualGrid")
					posX += gridSize
					# print((i, j))
				posY += gridSize				

			count = 0
			for box in self.__gridSpot:
				# print(box)
				x, y = box
				self.__render.create_text(x+(gridSize/2), y+(gridSize/2), text=str(count), tag="GlobalTxt")
				count+=1
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
		Required Arguments
		------------------
		|	- index - *int* - Specific index in the gridSpot list
		Methods Return
		--------------
			The entire list gridSpot or gridSpot[@index].
		"""
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

