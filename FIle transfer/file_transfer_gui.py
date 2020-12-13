
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import shutil
import os
import sys 
import time
import datetime
import sqlite3


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
    
        self.btn_source = tk.Button(self.master,width=12,height=2,text='Browse',command=lambda:sourceFolder(self))        
        self.btn_source.grid(row=4,column=0,padx=(10,10),pady=(10,10),sticky=W)
        
        self.btn_destination = tk.Button(self.master,width=12,height=2,text='Browse',command=lambda:destinationFolder(self)) 
        self.btn_destination.grid(row=6,column=0,padx=(10,10),pady=(10,10),sticky=W)

        self.btn_fileTransfer = tk.Button(self.master,width=12,height=2,text='Transfer',command=lambda: fileTransfer(self))
        self.btn_fileTransfer.grid(row=4,column=2,padx=(10,10),pady=(10,10),sticky=W)

        self.btn_close = tk.Button(self.master,width=12,height=2,text='close',command= exit)
        self.btn_close.grid(row=6,column=2,padx=(10,10),pady=(10,10),sticky=W)

        
        self.custom_source = StringVar()
        self.custom_source.set('Select a source directory')

        self.txt_source = tk.Entry(self.master,textvariable=self.custom_source)
        self.txt_source.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(10,10),pady=(10,10),sticky=N+E+W)



        self.custom_destination = StringVar()
        self.custom_destination.set('Select a destination directory')
        
        self.txt_destination = tk.Entry(self.master,text=self.custom_destination)
        self.txt_destination.grid(row=2,column=0,rowspan=1,columnspan=2,padx=(10,10),pady=(10,10),sticky=N+E+W)

        self.lbl_user = tk.Label(self.master,text='Source folder: ')
        self.lbl_user.grid(row=3,column=0,padx=(0,0),pady=(0,0))

        self.lbl_user = tk.Label(self.master,text='Destination folder:')
        self.lbl_user.grid(row=5,column=0,padx=(0,0),pady=(0,0))

        


        def sourceFolder(self):
            self.txt_source.delete(0, END)
            folder = filedialog.askdirectory()
            self.txt_source.insert(0, folder)



        def destinationFolder(self):
            self.txt_destination.delete(0, END)
            folder = filedialog.askdirectory()
            self.txt_destination.insert(0, folder)




        def fileTransfer(self):
            custom_source = self.txt_source.get()
            custom_destination = self.txt_destination.get()

            now = datetime.datetime.now()
            ago = now - datetime.timedelta(hours=24)
            print('The following .txt files were modified in the last 24 hours: \n')
            for files in os.listdir(custom_source):
                if files.endswith('.txt'):
                    path = os.path.join(custom_source, files)
                    st = os.stat(path)
                    mtime = datetime.datetime.fromtimestamp(st.st_mtime)
                    if mtime > ago:
                        print('{} ~ last modified {}'.format(path, mtime))
                        file_source = os.path.join(custom_source, files)
                        file_destination = os.path.join(custom_destination, files)
                        shutil.move(file_source, file_destination)
                        print("\tMoved {} to {}.\n".format(files, custom_destination))
                        current_time = time.time()
            
                        
                        
                            
                        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()














    
