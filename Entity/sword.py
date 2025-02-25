from Engine import eNode
import keyboard

class sword(eNode):
	"""
	sword known as sword
	Parent Class: eNode(entityNode.py)
	Class Variables:
		(any from eNode) 
		private: 
			.__myID
		protected: None
		public: None
	Description: Houses spcfic information of the sword entity.
	"""
	def __init__(self, render):
		super().__init__(render)
		self.__myID = "sword#1"
