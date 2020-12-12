
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import shutil
import os
import sys 
import time

source = '/Users/lyonb/Desktop/FileCheck/Folder A/'
destination = '/Users/lyonb/Desktop/FileCheck/Folder B/'
files = os.listdir(source)
for i in files:
    shutil.copy(source+i, destination)

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
        self.lbl_body = tk.Label(self.master,text='Added Here ')
        self.lbl_body.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

        self.txt_body = tk.Entry(self.master,text='')
        self.txt_body.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

        self.btn_add = tk.Button(self.master,width=12,height=2,text='Search',command= FileCheck2)
        self.btn_add.grid(row=2,column=0,padx=(25,0),pady=(25,10),sticky=W)
        
        self.btn_add = tk.Button(self.master,width=12,height=2,text='Check Daily',command= browseFiles)
        self.btn_add.grid(row=3,column=0,padx=(25,0),pady=(25,10),sticky=W)

        self.btn_add = tk.Button(self.master,width=12,height=2,text='Copied Files',command= browseFiles2)
        self.btn_add.grid(row=2,column=2,padx=(25,0),pady=(25,10),sticky=W)

        self.btn_add = tk.Button(self.master,width=12,height=2,text='File Check',command= FileCheck)
        self.btn_add.grid(row=3,column=2,padx=(25,0),pady=(25,10),sticky=W)


    
def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/Users/lyonb/Desktop/FileCheck/Folder A", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))

def browseFiles2(): 
    filename = filedialog.askopenfilename(initialdir = "/Users/lyonb/Desktop/FileCheck/Folder B", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))

def FileCheck():
    filename = '/Users/lyonb/Desktop/FileCheck/Folder A'
    statbuf = os.stat(filename)
    print("Modification Time: {}".format(statbuf.st_mtime))

def FileCheck2():
    filename = txt_body
    statbuf = os.stat(filename)
    print("Modification Time: {}".format(statbuf.st_mtime))



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()



    
