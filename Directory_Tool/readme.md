!['image'](https://github.com/CreativeDave/The-Tech-Academy-Python-Coding-Projects/blob/master/Directory_Tool/media/Directory_Tool.gif)

# Directory Tool

> A tkinter tool that identifies all .txt files in a chosen directory and moves them to a new one. It then creates a database and inserts the file name and time of modification.

## Project Overview

This basic application consists of 3 .py files: 
- [tool_main](https://github.com/CreativeDave/The-Tech-Academy-Python-Coding-Projects/blob/master/Directory_Tool/Directory_Tool_main/tool_func.py) 
- [tool_gui](https://github.com/CreativeDave/The-Tech-Academy-Python-Coding-Projects/blob/master/Directory_Tool/Directory_Tool_main/tool_gui.py)
- [tool_func](https://github.com/CreativeDave/The-Tech-Academy-Python-Coding-Projects/blob/master/Directory_Tool/Directory_Tool_main/tool_func.py)

The zen of python states, "explicit is better than implicit," So the first thing do call an instance of Tk and create the root window from the tool_main file. 
```
if __name__ == "__main__":
    root = tk.Tk()
    App = Window(root)
    root.mainloop()
 ```

Tool_main.py defines a Window class with an __init__ function that calls tool_gui.py 
```
class Window(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(515,175)
        self.master.maxsize(1030,325)
        self.master.title("Directory Tool")
        self.master.configure(bg="light gray")
        
# calls load_gui function from tool_gui to populate widgets
        tool_gui.load_gui(self) 
   ```
Tool_gui populates the frame with widgets and creates the interface for the user to engage.  Specific actions, like clicking a buton, will call a lambda funtion to tool_func.py. 

For example, when the top browse button is clicked, the *search_dir* function is called which asks the user to choose a directory, then stores the path as a string variable. 
```
# gets the first chosen directory that the files will be selected from
def search_dir(self):
    directory = askdirectory()
    if directory:
        self.varDir.set(directory)
 ```
The bottom browse button does essentially the same thing, only it stores the destination directory with *search_dest.*
     
The following code creates a 'transfer files' button which calls the *iterate* function when clicked. 

```
    self.btn_check = tk.Button(self.master,width=12,height=2,text='Transfer files...', command=lambda: tool_func.iterate(self))
    self.btn_check.grid(row=4,column=0,padx=(20,0),pady=(5,0),sticky=N+W)
```

Iterate does a couple things and is a really fun function. When called, 

1. It takes the directory defined from search_dir, then uses os.listdir to create a list of the items in it. 
2. It then iterates through these items looking for files that end in .txt, 
3. It appends them to an array, then uses shutil.move to change the directory to the desitination directory defined in search_dest
4. Finally, getmtime is called to get the time the file was moved, appends it to a dictionary for each file, then passes the dictionary on to another function that creates a database of this information.
```
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
```


