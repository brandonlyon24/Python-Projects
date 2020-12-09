# Python    3.5.1
#
# Author:   Brandon Lyon
#
# Purpose:  Creating a phone book demonstrating OOP, Tkinker module
#           using tkinter parent and child relationships
#
from tkinter import *
import tkinter as tk

import phonebook_gui
import drill50_phonebook_func

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Master frame configuration
        self.master = master
        self.masterminsize(500,300) #Height and width
        self.master.maxsize(500,300)
        # This centerwindow method will center the app on the users screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phone book app!")
        self.master.configure(bg="#FOFOFO")
        # This protocol method is a tkinter built-in method to catch
        # if the user clicks the upper corner X on windows os
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a seprate module
        phonebook_gui.load_gui(self)
    

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
