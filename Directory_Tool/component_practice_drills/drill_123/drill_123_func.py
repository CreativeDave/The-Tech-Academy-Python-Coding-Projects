import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory

import drill_123_main
import drill_123_gui




def search_dir(self):
    directory = askdirectory()
    if directory:
        self.varDir.set(directory)

def search_dest(self):
    destination = askdirectory()
    if directory:
        self.varDest.set(destination)
        
    




if __name__ == "__main__":
    pass
