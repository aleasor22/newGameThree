from .kineticsNode import kNode
from .imageNode import iNode

class eNode(kNode):
	"""
	eNode known as Entity Node
		Parent Class: kNode(kineticsNode.py)
		Variables:
			(any from kNode) 
			private: None
			protected:
				_speed = storage of how "fast" the object moves
				_entityTag = (str) stores a general tag name that specifies a group of objects
			public: None
			
	"""
	def __init__(self, canvas):
		super().__init__(canvas)
		self._speed = 0
		self._entityTag = None

	def entitySetUp(self, imgName, entityTag, uniqueID, coords, static=False):
		"""
		Method: entitySetUp
			req. Arguments:
				imgName = the file name that houses the png displayed on screen.
				entityTag = (str) that refers to the group tag used for every instance of object.
				uniqueID = (str) that refers to specific instance of object.
				coords = (x, y) tupe to represent where the image is displayed to. (Top-Left Corner)
				static = Set to true when the object cannot move. (default == False)
		Description: 
			Used to set and store entity level tags and parameters.
		Returns: Nothing
		"""

		self.imageCreate("z_Pictures\\" + str(imgName))
		self.imagePlace(coords)
		self._entityTag = entityTag #NOTE do I need this?
		self.createImageTag(entityTag)
		self.createImageTag(uniqueID)
		self._coords = coords
		self._isStatic = static #Default is true

	def get_bbox(self):
		"""Returns self.bbox of the object that called this method"""
		#tkinter method .bbox returns top-left and bottom-right corners of target object.
		return self._render.bbox(self._imageID)

	#NOTE do I need it?
	def get_coords(self):
		"""Returns self._coords"""
		return self._coords

	#NOTE do I need it?
	def get_size(self):
		"""Returns self._size"""
		return self._size

	def get_center(self):
		"""Returns tuple (x, y) of objects center"""
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
		"""Returns list of tuples for each coordanate of each sides midpoint"""
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
		"""Returns either a list of tags [groupID, uniqueID] or tag at index: tagLevel"""
		if tagLevel == None:
			return self._render.gettags(self._imageID) #returns a list of tags [groupID, uniqueID]
		else:
			return self._render.gettags(self._imageID)[tagLevel] #returns tag at index: tagLevel

	def get_speed(self):
		"""Returns self._speed"""
		return self._speed

	#sets self._coords to coords
	def set_coords(self, coords):
		"""Sets coords to self._coords"""
		self._coords = coords
