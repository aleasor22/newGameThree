

class dNode(): ##ENTIRE PURPOSE OF THIS CLASS IS TO SAVE DATA TO BE ACCESSED AGAIN
	def __init__(self):
		self.fileDir = None
		self.pilImage = None
		self.tkImage = None


	def imageInfo(self, fileDir, pilImage, tkImage):
		self.fileDir = fileDir
		self.pilImage = pilImage
		self.tkImage = tkImage