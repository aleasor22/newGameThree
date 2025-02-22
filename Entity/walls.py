from Engine import eNode

class walls(eNode):
	def __init__(self, render, tag):
		super().__init__(render)
		self.tagNumber = "wall#" + str(tag) # enemyOne tags will start at 0, max 9999

	def wallSetUp(self, coords):
		#generates required data set for image
		self.entitySetUp("wall02.png", "staticWall", self.tagNumber, coords, True)
