
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import shutil
import os
import sys 
import time


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        self.master.title("File Transfer")
        self.master.configure(bg="#F0F0F0")
        arg = self.master
        self.load_gui()

    def load_gui(self):
    
        self.btn_add = tk.Button(self.master,width=12,height=2,text='Browse',command=lambda:sourceFolder(self))        
        self.btn_add.grid(row=4,column=0,padx=(10,10),pady=(10,10),sticky=W)
        
        self.btn_add = tk.Button(self.master,width=12,height=2,text='Browse',command=lambda:destinationFolder(self)) 
        self.btn_add.grid(row=6,column=0,padx=(10,10),pady=(10,10),sticky=W)

        self.btn_add = tk.Button(self.master,width=12,height=2,text='Transfer')#,command= fileTransfer(self))
        self.btn_add.grid(row=4,column=2,padx=(10,10),pady=(10,10),sticky=W)

        self.btn_add = tk.Button(self.master,width=12,height=2,text='close',command= exit)
        self.btn_add.grid(row=6,column=2,padx=(10,10),pady=(10,10),sticky=W)


        self.txt_fname = tk.Entry(self.master,text='')
        self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(10,10),pady=(10,10),sticky=N+E+W)
        
        self.txt_lname = tk.Entry(self.master,text='')
        self.txt_lname.grid(row=2,column=0,rowspan=1,columnspan=2,padx=(10,10),pady=(10,10),sticky=N+E+W)

        self.lbl_user = tk.Label(self.master,text='Source folder: ')
        self.lbl_user.grid(row=3,column=0,padx=(0,0),pady=(0,0))

        self.lbl_user = tk.Label(self.master,text='Destination folder:')
        self.lbl_user.grid(row=5,column=0,padx=(0,0),pady=(0,0))


        def sourceFolder(self):
            folder = filedialog.askdirectory()
            self.txt_fname.delete(0, END)
            self.txt_fname.insert(0, folder)



        def destinationFolder(self):
            folder = filedialog.askdirectory()
            self.txt_lname.delete(0, END)
            self.txt_lname.insert(0, folder)
                
                


        def fileTransfer():
            modification_time = os.path.getmtime(path)
            local_time = time.ctime(modification_time)
            #get all modified in folder
            files = os.listdir(source)
            for i in files:
                shutil.copy(source+i, destination)
            print("Last file modification time:", local_time) 



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()














    
