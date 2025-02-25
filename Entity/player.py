from Engine import eNode
import keyboard

class Player(eNode):
	"""
	Player known as Player
	Parent Class: eNode(entityNode.py)
	Class Variables:
		(any from eNode) 
		private: 
			.__myID
		protected: None
		public: None
	Description: Houses spcfic information of the player entity.
	"""
	def __init__(self, render):
		super().__init__(render)
		self.__myID = "player#1"

	def playerSetUp(self, coords):
		"""
		Method: playerSetUp
		req. Arguments: coords = tuple (x, y) coordinates where the image will be first placed.
		Description: Generates required data set for image
		Returns:
		"""
		self.entitySetUp("player.png", "player", self.__myID, coords)
		self._speed = 10


	def playerMove(self):
		"""
		Method: playerMove
		req. Arguments: None
		Description: How the user controls the player entity. 
		Returns: None
		"""
		if keyboard.is_pressed('a') == True:
			self._coords = self.controlledMove("left", self._speed)
		if keyboard.is_pressed('d') == True:
			self._coords = self.controlledMove("right", self._speed)
		if keyboard.is_pressed('w') == True:
			self._coords = self.controlledMove("up", self._speed)
		if keyboard.is_pressed('s') == True:
			self._coords = self.controlledMove("down", self._speed)
