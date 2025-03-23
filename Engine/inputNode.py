from pynput import keyboard, mouse
from .eventsNode import evNode
from tkinter import *
import pygetwindow


class inNode(evNode):
	def __init__(self, mainApp, canvas, root,  widget):
		##----CLASS SPECIFIC CALLS----##
		##requested Variables from other classes
		evNode.__init__(self, mainApp=mainApp, rootPath=root, canvas=canvas)
		self.widget = widget 
		
		##----START OF CLASS VARIABLES
		self.__listeningStarted = False
		self.local_x = 0 #mouse x posiiton. NOTE: Only updates when inside the tk window
		self.local_y = 0 #mouse y posotion. NOTE: Only updates when inside the tk window
		##----END OF CLASS VARIABLES----##

		# ##----START OF SHORTCUTS----##
		self.__allHotKeys = {
			## File Functions
			"<ctrl>+<shift>+s" : self.saveFile, ##Hotkey to save file as...
			"<ctrl>+s" : lambda: self.saveFile(saveAs=False), ##Hotkey to save file
			"<ctrl>+o" : self.openFile, ##Hotkey to open file
			"<ctrl>+n" : lambda:self.newFile(txt="hello"), ##Hotkey create new file
			## Edit Functions
			"<ctrl>+x" : lambda: self.printMsgToScreen(optionalTxt='cut'), ##Hotkey to cut item to clipboard
			"<ctrl>+c" : lambda: self.printMsgToScreen(optionalTxt='copy'), ##Hotkey to copy item to clipboard
			"<ctrl>+v" : lambda: self.printMsgToScreen(optionalTxt='paste'), ##Hotkey to paste item from clipboard
			"<ctrl>+z" : lambda: self.printMsgToScreen(optionalTxt='undo'), ##Hotkey to undo last action
			"<ctrl>+y" : lambda: self.printMsgToScreen(optionalTxt='redo'), ##Hotkey to redo last action
			#"<delete>" : self.,  ##Hotkey to delet objects from screeen. 
		}
		##----END OF SHORTCUTS----##


		##----PYNPUT LIBRARY CALLS----#
		##Calls Listener Class, initiallizing the following functions
		self.__keyboardListen = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
		self.__hotKeysListen = keyboard.GlobalHotKeys(self.__allHotKeys)
		# self.__mouseListen = mouse.Listener(on_click=self.on_click,)

		##Starts listening for keyboard & mouse events
		# self.__mouseListen.start()
		self.__keyboardListen.start()
		self.__hotKeysListen.start()

	

	##----START OF GENERAL INPUT METHODS----##
	# def 
	def startListening(self):
		if self.__listeningStarted:
			pass
		else:
			self.__listeningStarted = True ##Sets listenintStarted to true

			##New Instances for threading. 
			self.__keyboardListen = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
			self.__hotKeysListen = keyboard.GlobalHotKeys(self.__allHotKeys)

			##Starts the threads
			self.__keyboardListen.start()
			self.__hotKeysListen.start()
		

	def stopListening(self):
		self.__listeningStarted = False ##Sets listeningStarted to False
		##Stops the threads
		self.__keyboardListen.stop()
		self.__hotKeysListen.stop()


	def bindAllEvents(self, ):
		self._render.bind('<Enter>', self.inRender)
		self._render.bind('<Leave>', self.outRender)
		self._render.bind('<Motion>', self.positionInRender)
		self._render.bind('<Button-1>', self.onM1Press)
		self._render.bind('<Button-2>', self.onM3Press)
		self._render.bind('<Button-3>', self.onM2Press)
		self._render.bind('<MouseWheel>', self.mouseScroll)

	def unBindAllEvents(self, ):
		self._render.unbind('<Enter>')
		self._render.unbind('<Leave>')
		self._render.unbind('<Motion>')
		self._render.unbind('<Button-1>')
		self._render.unbind('<Button-2>')
		self._render.unbind('<Button-3>')
		self._render.unbind('<MouseWheel>')
		# print("unbinded events")

	##----END OF GENERAL INPUT METHODS----##

	##----START OF KEYBOARD----#
	##----PYNPUT METHODS----##
	def on_press(self, key):
		# print('L')
		try:
			print('alphanumeric key {0} pressed'.format(key.char))
		except AttributeError:
			print('special key {0} pressed'.format(key))
		pass


	def on_release(self, key):
		# print('{0} released'.format(key))

		##kills program based on this if statement
		try:
			
			if key.char == 'q':
				# Stop listener
				self.stopListening()
				self.unBindAllEvents()
				self._mainApp.quit()
			print('alphanumeric key {} released'.format(key.char))
				# return False
		except AttributeError:
			if key == keyboard.Key.esc:
				self.stopListening()
				self.unBindAllEvents()
				self._mainApp.quit()
			print('special key {0} released'.format(key))
		
	##----END OF KEYBOARD----#

	##----START OF GETTERS----#
	def get_insideTkinter(self):
		return self.__isInRender
	
	def get_activeWindowTitle(self):
		try:
			# print(pygetwindow.getActiveWindow().title)
			return pygetwindow.getActiveWindow().title
		except AttributeError:
			print("Window Can't be of NoneType")
	
	# def get_mousePosition(self):
	# 	return pos)