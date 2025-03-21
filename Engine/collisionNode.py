class cNode(): 
	"""
	Colisison Node
	==============
	Class Parameters
	----------------
	| 	- render - *private* - Base level canvas created using tkinter
	|	- allObjects - *private* - Python dictionary that houses all available objects in the codebase
	|	- multipleIds - *public* - TBD
	Class Description
	------------------
		This handles all collision events inside the game, if an entity is overlapping with another entity this code runs. 
	"""
	def __init__(self, render):
		self.__render = render #this is the main canvas created in "mainTkinter.py"
		self.__allObjects = {}
		self.multipleIds = []


	#use: self.__render.find_overlapping(x1, y1, x2, y2)
	#Identifies if objects are overlapping, therefor, colliding
	def isColliding(self, targetObject):
		"""
		Method Arguments
		----------------
		|	- targetObject - *obj* - Object that is checking for collision
		Method Description
		-----------
			Finds the bbox (coords corisponding to the outline of the object) and uses this bbox to see if tkinters canvas has more than one object in the same box of coords. Then adds the resulting list of objects to the list -> "listOfTags"
		Methods Return
		-------------
		|	- self.multipleIds - *list of type: int* - If collision happend then the associated tags are appended to the list, for later referance. 
		"""
		listOfTags = []
		self.multipleIds = [] #resets list everytime method is called
		#returns the targetObjects top left and botom right corners
		x1, y1, x2, y2 = targetObject.get_bbox()

		#returns a tuple of every canvasID within targetObjects bbox, including itself.
		tupleOfCanvasIds = self.__render.find_overlapping(x1, y1, x2, y2)

		#converts cancasID into the uniqueID
		#the important ID can now be identified using .gettag(1)
		for item in tupleOfCanvasIds:
			# print(self.__render.gettags(item)[1], "==", targetObject.gettag(1))
			if self.__render.gettags(item)[1] != targetObject.gettag(1):
				listOfTags.append(self.__render.gettags(item)[1])
				# print(self.__render.gettags(item)[1], "==", targetObject.gettag(1))
		# print(listOfTags, "and", targetObject.gettag(1))

		if len(listOfTags) == 1:
			self.multipleIds.append(listOfTags[0]) #returns list of tags with specificd objectID
			return self.multipleIds #returns uniqueID
		else: #happens when listOfTags is greater than 1
			for item in listOfTags:
				self.multipleIds.append(item)
			return self.multipleIds


	def collisionDirection(self, myTag, theirTagList):
		"""
		Required Arguments
		------------------
		|	- myTag - *str* - Identification of the "main" object to process collision.
		|	- theirTagList - *list of type: obj* - List that holds the rest of the colliding objects.
		Method Description
		-----------
			Used to determin which direction the main object should move based on where collision occured. This is done by comparing coordinates of the two or more objects that are colliding with each other.
		Method Return
		-------------
		|	- direction - *list of type: str* - List contains a strings that associate with a specific direction.
		"""
		#variable declaration
		direction = [] #creates a list to store each side that has collision
		myObject = self.__allObjects[myTag] #finds the object relating to "myTag"
		x, y = myObject.get_center() #calls myObjects's "get_center()" method, and stores the coords into x and y
		# print(self.__allObjects)

		#sideMidpoint[0] == top's coords
		#sideMidpoint[1] == right's coords
		#sideMidpoint[2] == bottom's coords
		#sideMidpoint[3] == left's coords
		if len(theirTagList) == 1:
			# print("1-on-1 collision")
			sideMidpoint = self.__allObjects[theirTagList[0]].get_edgesCenter()
			if x < sideMidpoint[3][0]:
				# print("left")
				direction.append("left")

			#myObject is hitting right side
			elif x > sideMidpoint[1][0]:
				# print("right")
				direction.append("right")

			#myObject is hitting top side
			elif y < sideMidpoint[0][1]:
				# print("top")
				direction.append("up")

			#myObject is hitting bottom side
			elif y > sideMidpoint[2][1]:
				# print("bottom")
				direction.append("down")

		else:
			for tag in theirTagList:
				#gets the midpoint of each side for object specificd by the tag
				sideMidpoint = self.__allObjects[tag].get_edgesCenter()

				#myObject is hitting left side
				if x < sideMidpoint[3][0] and y > sideMidpoint[0][1] and y < sideMidpoint[2][1]:
					# print("left")
					direction.append("left")

				#myObject is hitting right side
				elif x > sideMidpoint[1][0] and y > sideMidpoint[0][1] and y < sideMidpoint[2][1]:
					# print("right")
					direction.append("right")

				#myObject is hitting top side
				elif y < sideMidpoint[0][1] and x > sideMidpoint[3][0] and x < sideMidpoint[1][0]:
					# print("top")
					direction.append("up")

				#myObject is hitting bottom side
				elif y > sideMidpoint[2][1] and x > sideMidpoint[3][0] and x < sideMidpoint[1][0]:
					# print("bottom")
					direction.append("down")
			#end of loop

		# print(direction)
		return direction

	#finds the center point of a specified object
	#TODO may need to remove later?
	def get_trueCenter(self, tagOrId):
		"""
		Required Arguments
		----------------
		|   - tagOrId - *str* - Corresponds to a key inside the self.__allObjects dictionary
		Method Description
		-----------
			Using tagOrId this method will determin the coordinates of the center of the displayed object. returns tuple "center"
		Methods Return
		-------------
			center - *tuple - (x, y)* - Coords that corresponds to the center the the *tagOrId* object. 
		"""
		#using key tagOrId we find specified object
		targetObject = self.__allObjects[tagOrId]

		#recieving target objects parameters
		x, y = targetObject.get_coords()
		w, l = targetObject.get_size()

		#finding center of the object
		center = (x+int(w/2), y+int(l/2))
		# print(center, " :center of object", tagOrId)
		#returns the coords of the objects center
		return center

	def addObject(self, targetObject):
		"""
		Required Arguments
		----------------
		|   - targetObject - *obj* - Object that is to be added to dictionary __allObjects
		Method Description
		-----------
			Adds python object to dictionary __allObjects[key=targetObject's tag] = targetObject
		"""
		self.__allObjects[targetObject.gettag(1)] = targetObject
	


