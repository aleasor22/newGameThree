from pynput import keyboard, mouse
from tkinter import *


class inNode():
	def __init__(self, window, render, widget):
		##----CLASS SPECIFIC CALLS----##
		##requested Variables from other classes
		self.window = window #The tkinter main window object.
		self.render = render #The Canvas object
		self.widget = widget 
		
		##----START OF CLASS VARIABLES
		self.__activated = 0 ##Default = 0, anything else means the mouse is positioned inside the tk window
		self.__isInRender = False
		self.local_x = 0 #mouse x posiiton. NOTE: Only updates when inside the tk window
		self.local_y = 0 #mouse y posotion. NOTE: Only updates when inside the tk window
		##----END OF CLASS VARIABLES----##


		##----PYNPUT LIBRARY CALLS----#
		##Calls Listener Class, initiallizing the following functions
		self.__keyboardListen = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
		self.__mouseListen = mouse.Listener(on_click=self.on_click,)

		##Starts listening for keyboard & mouse events
		self.__mouseListen.start()
		self.__keyboardListen.start()

	##----START OF GENERAL INPUT METHODS----##
	def stopListening(self):
		self.__mouseListen.stop()
		self.__keyboardListen.stop()


	def bindAllEvents(self, ):
		self.render.bind('<Enter>', self.inRender)
		self.render.bind('<Leave>', self.outRender)
		self.render.bind('<Motion>', self.positionInRender)
		self.render.bind('<Button-3>', self.temp)

	def unBindAllEvents(self, ):
		self.render.unbind('<Enter>')
		self.render.unbind('<Leave>')
		self.render.unbind('<Motion>')
		self.render.unbind('<Button-3>')
		# print("unbinded events")

	##----END OF GENERAL INPUT METHODS----##

	##----START OF MOUSE----#
	def inRender(self, event):
		self.__isInRender = True
		print("Entered render at", (event.x, event.y))
		
	def outRender(self, event):
		self.__isInRender = False
		print("Left Render at", (event.x, event.y))

	def positionInRender(self, event):
		if self.__isInRender:
			# print(event.x, event.y)
			self.local_x = event.x
			self.local_y = event.y
		
	def temp(self, event):
		print(self.local_x, self.local_y, "Local")
		print(event.x_root, event.y_root, "Root")
		self.widget.get_editMenuList().post(event.x, event.y)
	
	def on_click(self, x, y, button, pressed):
		# if button == mouse.Button.right and self.__isInRender:
		# 	print("right-click")
			
		# 	test = Button(self.window, text="Test", command=lambda:test.bell())
		# 	test.place(x=self.local_x, y=self.local_y)
		# 	print(self.local_y, self.window.winfo_y(), self.window.winfo_height())
			
		# if button == mouse.Button.left:
		# 	print("Left-click")
		# 	print(self.local_x, self.local_y, "Local")
		pass

	def on_scroll(self, x, y, dx, dy):
		print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

	##----END OF MOUSE----#

	##----START OF KEYBOARD----#
	def on_press(self, key):
		try:
			if key.char == 'q':
				print('alphanumeric key {0} pressed'.format(key.char))
		except AttributeError:
			print('special key {0} pressed'.format(key))

	def on_release(self, key):
		print('{0} released'.format(key))

		##kills program based on this if statement
		try:
			if key.char == 'q':
				# Stop listener
				self.stopListening()
				self.unBindAllEvents()
				self.window.quit()
			print('alphanumeric key {} released'.format(key.char))
				# return False
		except AttributeError:
			if key == keyboard.Key.esc:
				self.stopListening()
				self.unBindAllEvents()
				self.window.quit()
			print('special key {0} pressed'.format(key))
		
	##----END OF KEYBOARD----#

	##----START OF GETTERS----#
	def get_insideTkinter(self):
		return self.__insideTkinter
	
	# def get_mousePosition(self):
	# 	return pos)