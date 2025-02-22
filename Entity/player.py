from Engine import eNode
import keyboard

class Player(eNode):
	def __init__(self, render):
		super().__init__(render)
		self.__myID = "player#1"
		pass

	def playerSetUp(self, coords):
		#generates required data set for image
		self.entitySetUp("player.png", "player", self.__myID, coords)
		self._speed = 10


	def playerMove(self):
		if keyboard.is_pressed('a') == True:
			self._coords = self.controlledMove("left", self._speed)
		if keyboard.is_pressed('d') == True:
			self._coords = self.controlledMove("right", self._speed)
		if keyboard.is_pressed('w') == True:
			self._coords = self.controlledMove("up", self._speed)
		if keyboard.is_pressed('s') == True:
			self._coords = self.controlledMove("down", self._speed)
