"""This is the main file that runs everything for the game
it's whateva tho
Everything else is run once outside of func gameLoop()"""

from Engine import *
from Entity import *
import keyboard
import random as rand

#creates a game loop to constantly check for inputs
def gameLoop():
	"""Anything that needs to be constantly updated will be inside here
	otherwise the code will only run once
	"""
	#Entity loops
	player.playerMove()
	#runs active game loop for each typeOne enemy
	for object in enemyTypeOne:
		object.enemyOneAi()

	#checks for collision
	#start of enemy's collision logic
	for enemy in enemyTypeOne:
		enemyCollision = cNode.isColliding(enemy)
		if enemyCollision != []:
			# print(enemyCollision, "enemyCollision 0")
			enemyDirection = cNode.collisionDirection(enemy.gettag(1), enemyCollision)
			if enemyDirection != None:
				for string in enemyDirection:
					enemy.set_coords(enemy.knockBack(string, enemy.get_speed()))
				# for tag in enemyCollision:
				# 	enemy.set_coords(enemy.knockBack(enemyDirection[tag][0], enemy.get_speed()))
	#end of enemy's collision logic
	
	#start of player's Collision logic
	playerCollision = cNode.isColliding(player)
	if playerCollision != []:
		# print(playerCollision, "playerCollision")
		# print(playerCollision)
		playerDirection = cNode.collisionDirection(player.gettag(1), playerCollision)
		if playerDirection != None:
			for string in playerDirection:
				player.set_coords(player.knockBack(string, player.get_speed()))
	else:
		player.resetDisabledDirections()

	#end of player's collision logic


	#Kill switch
	if keyboard.is_pressed('q') == True:
		TKINTER.closeWindow()


	TKINTER.get_mainApp().after(int(TKINTER.get_FPS()), gameLoop)
	#end of gameLoop


#main variable creation
enemyTypeOne = [] #stores a list of every typeOne Enemy object
wallTypeStatic = [] #stores a list of every wallTypeStatic object

print('\n\n\n')
print('<<----------------------------->>')
print('<<-------Initial Set UP-------->>')
print('<<----------------------------->>')
#calls classes
TKINTER = mainApplication("Dungeon_Crawler [v0.0.41]", )
cNode = cNode(TKINTER.get_render())
player = Player(TKINTER.get_render())

#creates Grid
TKINTER.createGrid()

#adds new typeOne enemy to list of objects.
enemyTypeOne.append(enemyOne(TKINTER.get_render(), 0))
# enemyTypeOne.append(enemyOne(TKINTER.get_render(), 1))

#adds new typeStatic wall to list of objects
for i in range(7):
	wallTypeStatic.append(walls(TKINTER.get_render(), i))
# wallTypeStatic.append(walls(TKINTER.get_render(), 0))
# wallTypeStatic.append(walls(TKINTER.get_render(), 1))

print('\n<<-----Game Main Loop------>>\n')

player.playerSetUp((600, 100))
#sets up every typeOne enemy
for object in enemyTypeOne:
	randomCoords = TKINTER.get_gridSpot(rand.randint(0, len(TKINTER.get_gridSpot())))
	object.enemyOneSetUp(randomCoords)
	print(randomCoords, object.gettag(1), "coord, object")
#setUp for staticType walls
wallTypeStatic[0].wallSetUp(TKINTER.get_gridSpot(84))
wallTypeStatic[1].wallSetUp(TKINTER.get_gridSpot(85))
wallTypeStatic[2].wallSetUp(TKINTER.get_gridSpot(86))
wallTypeStatic[3].wallSetUp(TKINTER.get_gridSpot(87))
wallTypeStatic[4].wallSetUp(TKINTER.get_gridSpot(88))
wallTypeStatic[5].wallSetUp(TKINTER.get_gridSpot(66))
wallTypeStatic[6].wallSetUp(TKINTER.get_gridSpot(106))

#adds all objects to collision node's dictionary
#adds every enemyTypeOne object
for object in enemyTypeOne:
	cNode.addObject(object)
#adds every wall object
for object in wallTypeStatic:
	cNode.addObject(object)
#adds player's object
cNode.addObject(player)


#testing methods
# cNode.isOverLapping(player)
# cNode.get_trueCenter(player.gettag(1))


gameLoop()
TKINTER.windowSetUp() #End of call system



print('\n')
print('<<----------------------------->>')
print('<<-------------END------------->>')
print('<<----------------------------->>')
