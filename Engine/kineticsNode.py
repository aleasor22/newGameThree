from .imageNode import iNode

class kNode(iNode):
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
		x, y = myCoords
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
		return self._isStatic

	def get_isStunned(self):
		return self._isStunned

	def set_isStunned(self, isStunned):
		self._isStunned = isStunned

	def resetDisabledDirections(self):
		self._rightDisabled = False
		self._leftDisabled = False
		self._upDisabled = False
		self._downDisabled = False
