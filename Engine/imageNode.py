from tkinter import * #requires tk for image work.
from PIL import ImageTk, Image #PIL = Pillow

class iNode():
	"""
	Docstring for iNode.
	"""

	def __init__(self, canvas):
		self._render = canvas
		self._imageID = None #id assinged from _render.create_image method
		self._size = None
		self._coords = None
		self._pilImage = None
		self._tkImage = None

	#creates an image file for python to render and use
	#returns the PIL and tk images "ID" and size of image
	def imageCreate(self, imgLocation):
		self._pilImage = Image.open(str(imgLocation))
		self._size = self._pilImage.size
		self._tkImage = ImageTk.PhotoImage(self._pilImage)


	def imagePlace(self, coords):
		x, y = coords
		self._imageID = self._render.create_image(x, y, image=self._tkImage, anchor="nw")
		# self._render.addtag_withtag(imageTag, imageID) #adds a tangable tag to entity
		# return imageID

	def createImageTag(self, newTag):
		# print("new tag: ", newTag)
		self._render.addtag_withtag(newTag, self._imageID)

	def get_imageID(self):
		return self._imageID
