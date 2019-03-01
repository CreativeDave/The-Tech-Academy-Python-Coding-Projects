import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory

import drill_123_main
import drill_123_gui




def search_dir(self):
    directory = askdirectory()
    if directory:
        self.varSearch.set(directory)
    




if __name__ == "__main__":
    pass
