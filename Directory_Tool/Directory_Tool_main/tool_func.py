import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory

import tool_main
import tool_gui


def search_dir(self):

    def search_dir(self):
    directory = askdirectory()
    if directory:
        self.varDir.set(directory)

def search_dest(self):
    destination = askdirectory()
    if directory:
        self.varDest.set(destination)
    
