from .imageNode import iNode

class kNode(iNode):
	"""
	kNode known as Kinetics Node
	Parent Class: iNode(imageNode.py)
	Class Variables:
		(any non-private from iNode) 
		private: None
		protected: 
			._isStatic = Default False, True if the object static
			._isStunned = Default False, True if the object is "Stunned"
			._rightDisabled = Default False, If True the entity can't move in this direction
			._leftDisabled = Default False, If True the entity can't move in this direction
			._upDisabled = Default False, If True the entity can't move in this direction
			._downDisabled = Default False, If True the entity can't move in this direction
		public: 
			.myCoords
	Description: Background logic to allow for objects to move on screen.
	"""
	def __init__(self, canvas):
		super().__init__(canvas)
		self._isStatic = False #default is false
		self._isStunned = False
		#disabled DIRECTIONS
		self._rightDisabled = False
		self._leftDisabled = False
		self._upDisabled = False
		self._downDisabled = False


	def controlledMove(self, direction, speed):
		"""
		Method: methodName
		req. Arguments:
			direction = str, a string that tells what direction the object will move to.
			speed = int, an integer that determins how fast an object will move.
		Description: Sets up how an object gets to moved according to called moves within logic or user input.
		Returns: Returns tuple (x, y) - New coordinate location after the last movement.
		"""
		# print(myCoords, "my Coords?", ID)
		x, y = self._coords
		if direction == 'left' and self._leftDisabled == False:
			x -= 1 * speed
		if direction == 'right' and self._rightDisabled == False:
			x += 1 * speed
		if direction == 'up' and self._upDisabled == False:
			y -= 1 * speed
		if direction == 'down' and self._downDisabled == False:
			y += 1 * speed

		# print((x, y), ' :'+str(ID)+"'s Coords.")
		self._render.coords(self._imageID, x, y)
		return (x, y)

	def knockBack(self, direction, speed):
		"""
		Method: knockBack
		req. Arguments:
			direction = str, a string that tells what direction the knockback shouls move the object to.
			speed = int, a integer that determins how fast an object will move. 
		Description: Determins how far something should be knocked back after a collision even occurs
		Returns: Returns tuple (x, y) - New coordinate location after the last collision event.
		"""
		x, y = self._coords
		if direction == 'left':
			x -= 1 * speed
		elif direction == 'right':
			x += 1 * speed
		elif direction == 'up':
			y -= 1 * speed
		elif direction == 'down':
			y += 1 * speed
		else:
			print('NO DIRECTIONS')

		self._render.coords(self._imageID, x, y)
		return (x, y)


	def staticHit(self, direction):
		"""
		Method: staticHit
		req. Arguments:
			direction = str, a string that tells what direction that will be blocked. 
		Description: Prvents an object to move in the direction of something that is blocking it. 
		Returns: Returns tuple (x, y) - New coordinate location after the last collision event.
		"""
		x, y = self.myCoords #vscode is declaring this as an undefined variable, what/how is this used for?
		if direction == 'left':
			self._rightDisabled = True
		if direction == 'right':
			self._leftDisabled = True
		if direction == 'up':
			self._downDisabled = True
		if direction == 'down':
			self._upDisabled = True

		self.get_render().coords(self._imageID, x, y)
		return (x, y)

	def get_isStatic(self):
		"""Returns boolean self._isStatic"""
		return self._isStatic

	def get_isStunned(self):
		"""Returns boolean self._isStunned"""
		return self._isStunned

	def set_isStunned(self, isStunned):
		"""Sets isStunned to self._isStunned"""
		self._isStunned = isStunned

	def resetDisabledDirections(self):
		"""Resets the disabled directions back to their False default."""
		self._rightDisabled = False
		self._leftDisabled = False
		self._upDisabled = False
		self._downDisabled = False
