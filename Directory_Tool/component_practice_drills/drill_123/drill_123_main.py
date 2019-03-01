"""
Will search directory for a file then display file in search bar
"""


from tkinter import *
import tkinter as tk

import drill_123_gui
import drill_123_func




class Window(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(515,175)
        self.master.maxsize(515,175)
        self.master.title("Directory Search")
        self.master.configure(bg="#F0F0F0")

        drill_123_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = Window(root)
    root.mainloop()

        
