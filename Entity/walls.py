from Engine import eNode

class walls(eNode):
	"""
	walls known as Walls
	Parent Class: eNode(entityNode.py)
	Class Variables:
		(any from eNode) 
		private: None
		protected: None
		public: 
			.tagNumber = str, used to identify which wall is being interacted with. 
	Description: Houses spcfic information of the wall entity.
	"""
	def __init__(self, render, tag):
		super().__init__(render)
		self.tagNumber = "wall#" + str(tag) # enemyOne tags will start at 0, max 9999

	def wallSetUp(self, coords):
		#generates required data set for image
		self.entitySetUp("wall02.png", "staticWall", self.tagNumber, coords, True)
