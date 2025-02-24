from tkinter import * #requires tk for image work.
from PIL import ImageTk, Image #PIL = Pillow

class iNode():
	"""
	iNode known as Image Node
	Parent Class: None
	Class Variables:
		private: None
		protected: 
			._render = Canvas created by tkinter that is the deepest layer of the game\n
			._imageID = id assigned from the ._render.create_image()\n
			._size = (w, l) tuple that holds width & length of object\n
			._coords = (x, y) tuple that holds coordinates of the object\n
			._pilImage = object generated from calling .Image.open()\n
			._tkImage =  object generated from calling ImageTK.PhotoImage(._pilImage)\n
		public: None
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
		Method: imageCreate
		req. Arguments:
			imgLocation = (str) file location that stores target png 
		Description: Calling this method will take the target image and generate both a PILLOW and tkinter image as well as saving the generated objects size to class variables
		Returns: None
		"""
		self._pilImage = Image.open(str(imgLocation))
		self._size = self._pilImage.size
		self._tkImage = ImageTk.PhotoImage(self._pilImage)


	def imagePlace(self, coords):
		"""
		Method: imagePlace
		req. Arguments:
			coords = (x, y) tuple, The coordinates of where the image will be placed.
		Description: Method is used to place an image onto the canvas as specified location. 
		Returns: None
		"""
		x, y = coords
		self._imageID = self._render.create_image(x, y, image=self._tkImage, anchor="nw")
		# self._render.addtag_withtag(imageTag, imageID) #adds a tangable tag to entity
		# return imageID

	def createImageTag(self, newTag):
		"""
		Method: createImageTag
		req. Arguments:
			newTag =  str, name of object (???)
		Description: creates/add new tag to a image placed on the canvas
		Returns: None
		"""
		# print("new tag: ", newTag)
		self._render.addtag_withtag(newTag, self._imageID)

	def get_imageID(self):
		"""Returns self._imageID"""
		return self._imageID
