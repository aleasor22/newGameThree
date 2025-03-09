##IMPORTS START HERE
from ..imageNode import iNode
from PIL import ImageTk, Image
from tkinter import *
import tkinter as tk
import keyboard

##START OF EVENTS TKINTER CLASS
class eTkinter(iNode):
    """
    Events
    ==========
    Class Parameters
    ----------------
    |   - mainApp - *protected - obj* - the Tkinter display window where every widget it housed
    Class Description
    -----------------
        Where all the events that trigger in applications will be written and processed. 
    """
    def __init__(self, mainApp, RENDER):
        super().__init__(RENDER)
        self._mainApp = mainApp
        self._mainMenu = Menu(mainApp)

    
        