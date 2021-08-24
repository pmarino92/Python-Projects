# Python Ver:   3.9.2
#
# Author:   Phil A. Marino
#
#Purpose:   Phonebook demo. Demonstrating OOP, Tkinter GUI module,
#           using Tkinter Parent and Child relationship.
#
# Tested OS: Code was written and tested to work with Windows 10

from tkinter import *
import tkinter as tk

# Importing our other modules

import phonebook_gui
import phonebook_func

#Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500, 300) #(Height, Width)
        self.master.maxsize(500, 300)














if __name == "__main__":
