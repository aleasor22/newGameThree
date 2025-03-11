##IMPORTS START HERE
from .eventsTkinter import eTkinter
from PIL import ImageTk, Image
from tkinter import *
import tkinter as tk
import keyboard

##CLASS WIDGETS TKINTER STARTS HERE
class wTkinter(eTkinter):
    """
    Widgets
    ==========
    Class Parameters
    ----------------
    |   - TBD - *Priv/Pub/prot - noneType* - detailA
    Class Description
    -----------------
        Where all sorts of widgets will be housed. Ex. Buttons, Lable Frames, drop down menus, etc...
    """
    def __init__(self, mainApp, RENDER):
        super().__init__(mainApp, RENDER)
        pass

    ##----All widget methods except for Drop Down menus----##
    def buttonSetUp(self):
        """
        Required Arguments
        ------------------
        |   - variableA - *dataType* - detailA
        |   - variableB - *dataType* - detailB
        |   - variableC - *dataType* - detailC
        Method Description
        ------------------
            Where all the buttons shown on the application will get set up and packed to screen
        Methods Return
        --------------
            Returned Var - *data type* - Detail
        """
        ##----START OF METHOD----##
        ##Creating Label Frames
        frameOne = self.createLabelFrame(self._mainApp, "TEST-FRAME1")
        frameTwo = self.createLabelFrame(self._mainApp, "TEST-FRAME2")
        ##Creating Buttons
        TEST =  Button(self._mainApp, text="TestOne", )
        TEST2 =  Button(frameOne, text="TestTwo", )
        TEST3 =  Button(frameTwo, text="TestThree", )
        TEST4 =  Button(frameOne, text="TestFour", )

        ##Packs every widget to screen
        #RENDER is at grid(row=0, column=0, rowspan=1280, columnspan=768)
        frameOne.grid(row=0, column=769, rowspan=500)
        self.gridPropagateFalse([frameOne, ])
        TEST2.grid(row=0, column=0)
        TEST4.grid(row=0, column=1)
        TEST3.grid(row=1, column=1)
        print("button Size2?", self.get_buttonSize(TEST2))
        
        ##----END OF METHOD----##

    def createLabelFrame(self, parentWidget, name):
        """
        Required Arguments
        ------------------
        |   - name - *str* - Displayed name of the Frame Label
        |   - variableB - *dataType* - detailB
        |   - variableC - *dataType* - detailC
        Method Description
        ------------------
            Where all Label Frame widgets get created.
        Methods Return
        --------------
            newLabelFrame - *obj* - A Label Frame Object
        """
        ##----START OF METHOD----##
        newLabelFrame = LabelFrame(parentWidget, text=name, width=250, height=500, bg='Grey')

        return  newLabelFrame
        ##----END OF METHOD----##

    def gridPropagateFalse(self, objectsToPropagate):
        """
        Required Arguments
        ------------------
        |   - naobjectsToPropagateme - *list - obj* - List of objects to make grid_propagate(False)
        Method Description
        ------------------
            Where specified Label Frame widgets have propagate settings changed to False.
        """
        ##----START OF METHOD----##
        for obj in objectsToPropagate:
            obj.grid_propagate(False)
        ##----END OF METHOD----##

    ##----START OF GETTERS----##
    def get_buttonSize(self, buttonObject):
        """Returns (width, length) of the button once it has been displayed to screen"""
        return (buttonObject.winfo_width(), buttonObject.winfo_height())
    
    ##----ALL MENU DROP DOWN LOGIC----##
    def menusSetUp(self):
        """
        Required Arguments
        ------------------
        |   - variableA - *dataType* - detailA
        |   - variableB - *dataType* - detailB
        |   - variableC - *dataType* - detailC
        Method Description
        ------------------
            Where all the Drop Down menus will be set up and packed to screen
        Methods Return
        --------------
            Returned Var - *dataType* - Detail
        """
        ##----START OF METHOD----##

        ## Call menu methods in order left to right
        self.fileMenu()
        self.editMenu()
        self.windowMenu()
        self.tilesMenus()
        self.futureMenus()

        # self.compileMenuWidgets() ##Is this line needed?
        ##----END OF METHOD----##
        pass