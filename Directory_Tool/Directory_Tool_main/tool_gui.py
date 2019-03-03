
# Python Ver:   3.6.7
#
# Author:       David Wilson
#
# Purpose:      A basic tool that identifies all .txt files in
#               a chosen directory and moves them to a new one.
#               It then creates a database and inserts the file
#               name and time (getmtime) of modification.
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk
import os

import tool_main
import tool_func

# when called from tool_main, will create 2 browse buttons, 2 entry boxes, 1 transfer button, and 1 close button
def load_gui(self):

    self.varDir = StringVar()
    self.varDest = StringVar()

    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: tool_func.search_dir(self)) #creates browse button for direcotry
    self.btn_browse1.grid(row=2,column=0,padx=(20,0),pady=(45,10),sticky=N+W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: tool_func.search_dest(self)) #creates browse button for destination
    self.btn_browse2.grid(row=3,column=0,padx=(20,0),sticky=N+W)
    self.btn_check = tk.Button(self.master,width=12,height=2,text='Transfer files...', command=lambda: tool_func.iterate(self)) #creates transfer files button 
    self.btn_check.grid(row=4,column=0,padx=(20,0),pady=(5,0),sticky=N+W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: tool_func.closeApp(self)) # crates close button
    self.btn_close.grid(row=4,column=2,padx=(285,0))

    self.txt_search1 = tk.Entry(self.master,text=self.varDir,width=60) #creates entry box for first directory
    self.txt_search1.grid(row=2,column=1,columnspan=2,padx=(15,0),pady=(40,7))
    self.txt_search2 = tk.Entry(self.master,text=self.varDest, width=60) # creates destination box for second directory
    self.txt_search2.grid(row=3,column=1,columnspan=2,padx=(15,0),pady=(0,10))

 
if __name__ == "__main__":
   pass
