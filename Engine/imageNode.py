from tkinter import * #requires tk for image work.
from PIL import ImageTk, Image #PIL = Pillow

class iNode():
	"""
	Image Node
	==========
	Class Parameters
	----------------
	|   - render - *protected - obj* - Canvas created by tkinter that is the deepest layer of the application
	|   - imageID - *protected - TBD* - id assigned from the ._render.create_image()
	|   - size - *protected - tuple (w, l)* - Holds width & length of object
	|   - coords - *protected - tuple (x, y)* - Holds coordinates of the object
	|   - pilImage - *protected - obj* - Generated from calling .Image.open()
	|   - tkImage - *protected - obj* - Generated from calling ImageTK.PhotoImage(._pilImage)
	|
	Class Description
	-----------------
		Houses all methods that deal with creating and displaying an image to the application screen.
	"""
	def __init__(self, canvas):
		self._render = canvas	#Canvas created by tkinter that is the deepest layer of the game
		self._imageID = None	#id assinged from _render.create_image method
		self._size = None		#(w, l) tuple that holds width & length of object
		self._coords = None		#(x, y) tuple that holds coordinates of the object
		self._pilImage = None	#object generated from calling .Image.open()
		self._tkImage = None	#object generated from calling ImageTK.PhotoImage(._pilImage)

	#creates an image file for python to render and use
	#returns the PIL and tk images "ID" and size of image
	def imageCreate(self, imgLocation):
		"""
		Required Arguments
		------------------
		|   - imgLocation - *str* - File location that stores target png
		Method Description
		------------------
			Calling this method will take the target image and generate both a PILLOW and tkinter image as well as saving the generated objects size to class variables
		"""
		self._pilImage = Image.open(str(imgLocation))
		self._size = self._pilImage.size
		self._tkImage = ImageTk.PhotoImage(self._pilImage)


	def imagePlace(self, coords):
		"""
		Required Arguments
		------------------
		|   - coords - *tuple (x, y)* - The coordinates of where the image will be placed.
		Method Description
		------------------
			Method is used to place an image onto the canvas as specified location.
		"""
		x, y = coords
		self._imageID = self._render.create_image(x, y, image=self._tkImage, anchor="nw")
		# self._render.addtag_withtag(imageTag, imageID) #adds a tangable tag to entity
		# return imageID

	def createImageTag(self, newTag):
		"""
		Required Arguments
		------------------
		|   - newTag - *str* - The new tag that will be added to self.
		Method Description
		------------------
			Creates/Adds new tag to a image placed on the canvas
		"""
		self._render.addtag_withtag(newTag, self._imageID)

	def get_imageID(self):
		"""Returns self._imageID"""
		return self._imageID
