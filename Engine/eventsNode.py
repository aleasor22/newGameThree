##IMPORTS START HERE
from .imageNode import iNode
from .filesNode import fNode
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import keyboard

##START OF EVENTS TKINTER CLASS
class evNode(iNode, fNode):
    """
    Events Node
    ==========
    Class Parameters
    ----------------
    |   - mainMenu - *private - obj* - the Tkinter display view where every widget it housed
    |   - mainApp - *protected - obj* - the Tkinter object where all game based objects are housed
    |   - viewMenuList - *protected - obj* - Drop down group for "view"
    |   - futureMenuList - *protected - obj* - Drop down group for "Future"
    |   - fileMenuList - *protected - obj* - Drop down group for "File"
    |   - editMenuList - *protected - obj* - Drop down group for "Edit"
    |   - tilesList - *protected - obj* - Drop down group for "Tile"
    Class Description
    -----------------
        Where all the events that trigger in applications will be written and processed. 
    """
    def __init__(self, mainApp, RENDER, rootPath):
        iNode.__init__(self, canvas=RENDER)
        fNode.__init__(self, mainApp, rootPath)
        self.__mainMenu = Menu(mainApp) ##PARENT MENU OBJECT
        self._mainApp = mainApp ##PARENT TK OBJECT

        ##----DECLARATION OF MENUES----##
        self._viewMenuList    = Menu(self.__mainMenu, tearoff=False)  #TBD what is does
        self._futureMenuList    = Menu(self.__mainMenu, tearoff=False)  #Placeholder for future menus
        self._tilesMenuList     = Menu(self.__mainMenu, tearoff=False)  #TBD what it does
        self._fileMenuList      = Menu(self.__mainMenu, tearoff=False)  #Common File Operations
        self._editMenuList      = Menu(self.__mainMenu, tearoff=False)  #Common Edit Operations

        ##----WHAT IS THIS USED FOR?----##
        mainApp.config(menu=self.__mainMenu)
        ##----END OF INIT----##

    ##----SUBMENU LOGIC STARTS HERE----##
    def fileMenu(self):
        """
        Method Description
        ------------------
            Houses all the logic to goes into the "File" drop down menu.
        """
        ##----FILE LOGIC----#
        self.__mainMenu.add_cascade(label="File", menu=self._fileMenuList) ## Adds fileMenuList to main=Menu widget. 

        ##----START OF COMMAND LOGIC---##
        self._fileMenuList.add_command(label="New File...", command=self.newFile)
        self._fileMenuList.add_command(label="Open...", command=self.openFile)
        self._fileMenuList.add_command(label="Save...", command=lambda:self.saveFile(False))
        self._fileMenuList.add_command(label="Save as...", command=self.saveFile)
        self._fileMenuList.add_separator() #Spaces command options in a menu tab.
        self._fileMenuList.add_command(label="Exit", command=self._mainApp.quit)
        ##----END OF COMMAND LOGIC---##
         
    
    def editMenu(self):
        """
        Method Description
        ------------------
            Houses all the logic to goes into the "Edit" drop down menu.
        """
        ##----EDIT LOGIC----#
        self.__mainMenu.add_cascade(label="Edit", menu=self._editMenuList) ## Adds fileMenuList to main=Menu widget. 

        ##----START OF COMMAND LOGIC---##
        self._editMenuList.add_command(label="*FUTURE OPTION*", command=self.printMsgToScreen)
        ##----END OF COMMAND LOGIC---##

    def viewMenu(self):
        """
        Method Description
        ------------------
            Houses all the logic to goes into the "view" drop down menu.
        """
        ##----view LOGIC----##
        self.__mainMenu.add_cascade(label="View", menu=self._viewMenuList) ## Adds fileMenuList to main=Menu widget. 

        ##----START OF COMMAND LOGIC---##
        self._viewMenuList.add_command(label="*FUTURE OPTION*", command=self.printMsgToScreen)
        ##----END OF COMMAND LOGIC---##
    
    def futureMenus(self):
        """
        Method Description
        ------------------
            Houses all the logic to goes into the "Future" drop down menu.
        """
        ##----PLACEHOLDER DROPDOWNS----##
        self.__mainMenu.add_cascade(label="*FUTURE MENU*", menu=self._futureMenuList) ## Adds fileMenuList to main=Menu widget. 

        ##----START OF COMMAND LOGIC---##
        self._futureMenuList.add_command(label="*FUTURE OPTION*", command=self.printMsgToScreen)
        self._futureMenuList.add_separator() #Spaces command options in a menu tab.
        self._futureMenuList.add_command(label="*FUTURE OPTION*", command=self.printMsgToScreen)
        ##----END OF COMMAND LOGIC---##
        
    def tilesMenus(self):
        """
        Method Description
        ------------------
            Houses all the logic to goes into the "Tile" drop down menu.
        """
        ##----PLACEHOLDER DROPDOWNS----##
        self.__mainMenu.add_cascade(label="Tiles", menu=self._tilesMenuList) ## Adds fileMenuList to main=Menu widget. 

        ##----START OF COMMAND LOGIC---##
        self._tilesMenuList.add_command(label="*FUTURE OPTION*", command=self.printMsgToScreen)
        self._tilesMenuList.add_separator() #Spaces command options in a menu tab.
        self._tilesMenuList.add_command(label="*FUTURE OPTION*", command=self.printMsgToScreen)
        ##----END OF COMMAND LOGIC---##

    ##----START OF COMMAND METHODS----##
    def printMsgToScreen(self):
        """Prints a special message to screen"""
        print("**NO COMMAND YET**")

    
    ##----END OF COMMAND METHODS----##

    
        