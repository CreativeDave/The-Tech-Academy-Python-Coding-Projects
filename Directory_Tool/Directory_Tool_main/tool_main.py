
# Python Ver:   3.6.7
#
# Author:       David Wilson
#
# Purpose:      A basic tool that identifies all .txt files in
#               a chosen directory and moves them to a new one.
#               It then creates a database and inserts the file
#               name and time (getmtime) of modification.
#
# Tested OS:  This code was written and tested to work with Windows 10
#
# =====================================================================
#
# USE INSTRUCTIONS
#
# 1. All three .py files placed in same directory. DB will be created here.
# 2. The directory to be searched, and taret destination already exist.
# 3. Top browse is for the directory, bottom browse is for the destination.

from tkinter import *
import tkinter as tk

import tool_gui
import tool_func
import os

# creates the frame of the application
class Window(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(515,175)
        self.master.maxsize(1030,325)
        self.master.title("Directory Tool")
        self.master.configure(bg="light gray")
        
# calls load_gui function from tool_gui to populate widgets
        tool_gui.load_gui(self) #

if __name__ == "__main__":
    root = tk.Tk()
    App = Window(root)
    root.mainloop()
 
