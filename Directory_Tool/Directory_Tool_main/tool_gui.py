from tkinter import *
import tkinter as tk

import tool_main
import tool_func




def load_gui(self):

    self.varDir = StringVar()
    self.varDest = StringVar()

    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: tool_func.search_dir(self))
    self.btn_browse1.grid(row=2,column=0,padx=(20,0),pady=(45,10),sticky=N+W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: tool_func.search_dest(self))
    self.btn_browse2.grid(row=3,column=0,padx=(20,0),sticky=N+W)
    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check for files...')
    self.btn_check.grid(row=4,column=0,padx=(20,0),pady=(5,0),sticky=N+W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program')
    self.btn_close.grid(row=4,column=2,padx=(285,0))

    self.txt_search1 = tk.Entry(self.master,text=self.varDir,width=60)
    self.txt_search1.grid(row=2,column=1,columnspan=2,padx=(15,0),pady=(40,7))
    self.txt_search2 = tk.Entry(self.master,text=self.varDest, width=60)
    self.txt_search2.grid(row=3,column=1,columnspan=2,padx=(15,0),pady=(0,10))

 
if __name__ == "__main__":
   pass
