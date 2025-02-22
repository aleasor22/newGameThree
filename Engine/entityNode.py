from .kineticsNode import kNode
from .imageNode import iNode

class eNode(kNode):
	def __init__(self, canvas):
		super().__init__(canvas)
		self._speed = 0
		self._entityTag = None

	def entitySetUp(self, imgName, entityTag, uniqueID, coords, static=False):
		self.imageCreate("z_Pictures\\" + str(imgName))
		self.imagePlace(coords)
		self._entityTag = entityTag #NOTE do I need this?
		self.createImageTag(entityTag)
		self.createImageTag(uniqueID)
		self._coords = coords
		self._isStatic = static #Default is true

	def get_bbox(self):
		#tkinter method .bbox returns top-left and bottom-right corners of target object.
		return self._render.bbox(self._imageID)

	#NOTE do I need it?
	def get_coords(self):
		return self._coords

	#NOTE do I need it?
	def get_size(self):
		return self._size

	def get_center(self):
		x, y = self._coords
		w, l = self._size

		#finding center of the object
		center = (x+int(w/2), y+int(l/2))
		#returns the coords of the objects center
		return center

	#returns midpoint of each side of collision box
	#starts at top, then rotates clockwise
	#returns list [top, right, bottom, left] each one is a tuple of (x,y) coords of midpoint
	def get_edgesCenter(self):
		x, y = self._coords
		w, l = self._size

		#required math to find midpoint of each side
		top = (x+int(w/2), y)
		bottom = (x+int(w/2), y+l)
		left = (x, y+int(l/2))
		right = (x+w, y+int(l/2))

		#returns list of tuples for each coordanate of each sides midpoint
		return [top, right, bottom, left]

	def gettag(self, tagLevel=None):
		if tagLevel == None:
			return self._render.gettags(self._imageID) #returns a list of tags [groupID, uniqueID]
		else:
			return self._render.gettags(self._imageID)[tagLevel] #returns tag at index: tagLevel

	def get_speed(self):
		return self._speed

	#sets self._coords to coords
	def set_coords(self, coords):
		self._coords = coords
