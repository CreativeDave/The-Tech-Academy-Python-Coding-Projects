"""
Builds a basic form on the desktop using the tkinter module that takes 2 inputs,
first name, and last name, then prints a message to the user after the submit button
is pressed. Cancel clears the form and terminats the application.
"""


import tkinter
from tkinter import *

#parent class establishes attributes of frame
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter')
        self.master.config(bg='lightgray')

        self.varFname = StringVar()
        self.varLname = StringVar()
        
    #first name text indicates to the user what should be inputted
        self.lblFname = Label(self.master,text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.lblFname.grid(row=0, column=0,padx=(30,0), pady=(30,0))
        
    #last name ""
        self.lblLname = Label(self.master,text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.lblLname.grid(row=1, column=0,padx=(30,0), pady=(30,0))

    #establishes paramters of message after data is entered
        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0), pady=(30,0))
        
    #creates input box for first name
        self.txtFname = Entry(self.master,text=self.varFname, font=("Helvetica", 16), fg="black", bg="lightblue")
        self.txtFname.grid(row=0, column=1,padx=(30,0), pady=(30,0))
        
    #creates input box for last name
        self.txtLname = Entry(self.master,text=self.varLname, font=("Helvetica", 16), fg="black", bg="lightblue")
        self.txtLname.grid(row=1, column=1,padx=(30,0), pady=(30,0))
        
    #submit button placed below input
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1,padx=(0,0), pady=(30,0), sticky=NE)

    #cancel button placed below input to left of submit
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1,padx=(0,138), pady=(30,0), sticky=NE)
        
    #creates function for displaying message for to user 
    def submit(self):
        fn = self.varFname.get()
        ln = self.varLname.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))
        

    def cancel(self):
        self.master.destroy()



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
