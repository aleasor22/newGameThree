from PIL import ImageTk, Image
from tkinter import *
import tkinter as tk
import keyboard

class mainApplication():
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
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__screenWidth)+'x'+str(self.__screenHeight))
		self.createCanvas()
		# self.entitySetUp()
		self.__mainApp.mainloop()

	#background controlls
	def windowLoop(self):
		if keyboard.is_pressed('q') == True:
			self.closeWindow()
		self.__mainApp.after(int(self.__FPS), self.windowLoop)

	def closeWindow(self):
		self.__mainApp.quit()

	def createCanvas(self):
		self.__render.grid(row=0, column=0, )#rowspan=10)
		self.__render.grid_propagate(0)

	#default grid size to 32x32, 40x24 boxes  or 960 total boxes
	#default grid size of 64x64, 20x12 boxes  or 240 total boxes
	def createGrid(self, gridSize=64):
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
		return (self.__screenWidth, self.__screenHeight)

	def get_mainApp(self):
		return self.__mainApp

	def get_render(self):
		return self.__render

	def get_FPS(self):
		return self.__FPS

	def get_gridSpot(self, index=None):
		# print(len(self.__gridSpot))
		if index == None:
			return self.__gridSpot
		else:
			return self.__gridSpot[index]
