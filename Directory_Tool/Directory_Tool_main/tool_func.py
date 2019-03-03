
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


import sqlite3
import shutil
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory

import tool_main
import tool_gui


# gets the first chosen directory that the files will be selected from
def search_dir(self):
    directory = askdirectory()
    if directory:
        self.varDir.set(directory)
        
# gets the second chosen directory (destination) that the files will be moved to
def search_dest(self):
    destination = askdirectory()
    if destination:
        self.varDest.set(destination)
        
# iterates through all files in directory and chooses txt, then stores their name and getmtime into a dictionary
def iterate(self):
    txt_files = []
    txt_dic = {}
    directory = self.varDir.get()
    destination = self.varDest.get()
    filelist = os.listdir(path=directory)
    for file in filelist:
        if file.endswith('.txt'):
            txt_files.append(file)
            shutil.move(os.path.join(directory,file),destination) #moves files from directory to destination
            for name in txt_files: #creates absolute file path to be able to call getmtime
                apath = os.path.join(destination, name)
                mtime = os.path.getmtime(apath)
                txt_dic[name] = mtime
    makeDatabase(self, txt_dic)

#creates a database and inserts data into tables from the dictionary txt_dic.
def makeDatabase(self, txt_dic):
    conn = sqlite3.connect("file_record.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt_record( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_name TEXT, \
                    col_modified_time REAL)")
        for file, value in txt_dic.items():
            cur.execute("INSERT INTO tbl_txt_record (col_name,col_modified_time) VALUES (?,?)",
                        (file, txt_dic[file]))
            conn.commit()
        cur.execute("SELECT col_name, col_modified_time FROM tbl_txt_record")
        rows = cur.fetchall()
        for row in rows: #prints moved files to console with mtime
            print(row)
    conn.close()
    messagebox.showinfo("success!", "Any .txt files in chosen directory were successfully moved to: {}".format(self.varDest.get()))

def closeApp(self):
    messagebox.showinfo("Closing", "Goodbye!")
    self.master.destroy()
    os._exit(0)
 
    
    


if __name__ == "__main__":
    pass
    
