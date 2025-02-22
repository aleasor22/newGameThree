from Engine import eNode
import random as rand


class enemyOne(eNode):
	def __init__(self, render, tag):
		super().__init__(render)
		self.randomNum = rand.randint(0, 3)
		self.moveTime = 0 #"basic" movement for enemyOne
		self.__tag = "enemyType#1@" + str(tag) #id given for a spacific enemy
		# self.__tagNumber = 0 # enemyOne tags will start at 0, max 999
		# self.__allTags = []
		pass

	def enemyOneSetUp(self, coords):
		#generates required data set for image
		# print("enemy setup coords?", coords)
		self.entitySetUp("enemyOne.png", "enemyType#1", self.__tag, coords)
		self._speed = 5

	def enemyOneAi(self): #subject to change #README
		self.moveTime += 1
		if self.randomNum == 0:
			self._coords = self.controlledMove("right", self._speed)
		elif self.randomNum == 1:
			self._coords = self.controlledMove("down", self._speed)
		elif self.randomNum == 2:
			self._coords = self.controlledMove("left", self._speed)
		elif self.randomNum == 3:
			self._coords = self.controlledMove("up", self._speed)

		if self.moveTime == 40:
			self.randomNum = rand.randint(0, 3)
			self.moveTime = 0
