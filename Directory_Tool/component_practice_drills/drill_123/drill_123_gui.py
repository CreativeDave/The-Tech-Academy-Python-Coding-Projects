from tkinter import *
import tkinter as tk

import drill_123_main
import drill_123_func




def load_gui(self):

    self.varSearch = StringVar()

    self.txt_search = tk.Entry(self.master,text=self.varSearch,width=60)
    self.txt_search.grid(row=0,column=0,columnspan=4,padx=(75,0),pady=(40,40))

    self.btn_check = tk.Button(self.master,width=12,height=2,text='Search...',command=lambda: drill_123_func.search_dir(self))
    self.btn_check.grid(row=5,column=1,columnspan=2,padx=(65,0),pady=(0,10),sticky=S)



 
if __name__ == "__main__":
   pass
        
