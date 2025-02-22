import tkinter
import keyboard

class GUI_Main():
    def __init__(self, ):
        self._tk = tkinter.Tk()
        self.count = 0


    def launchWindow(self):
        self._tk.mainloop()

    def closeWindow(self):
        if keyboard.is_pressed('q'):
            self._tk.quic()

    def loopWindow(self):

        #shit goes HERE
        print("hello GUI_main")


        #close window
        self.closeWindow()


        #recursion
        #no recursion here
        # self._tk.after(int(100/30), self.loopWindow)


    def get_tk(self):
        return self._tk
