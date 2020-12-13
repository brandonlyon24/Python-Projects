
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

        self.btn_fileTransfer = tk.Button(self.master,width=12,height=2,text='Transfer',command=lambda: fileTransfer(self, self.custom_source, self.custom_destination))
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
            self.txt_source.insert(0, self.custom_source)



        def destinationFolder(self):
            folder = filedialog.askdirectory()
            self.txt_destination.delete(0, END)
            self.txt_destination.insert(0, self.custom_destination)





            def create_db(self):
                conn = sqlite3.connect('file_transfer.db')
                with conn:
                    c = conn.cursor()
                    c.execute("CREATE TABLE IF NOT EXISTS timestamps(unix REAL)")
                    conn.commit()
                    c.close()
                conn.close()

                def read_db(self):
                    conn = sqlite3.connect('file_transfer.db')
                    with conn:
                        c = conn.cursor()
                        c.execute("SELECT MAX(unix) FROM timestamps")
                        most_recent = c.fetchone()[0]
                        most_recent = time.ctime(most_recent)
                        c.close()
                    conn.close()

                    # create and populate the label_print widget
                    self.label_print = tk.Label(self.master, width=60, height=2, text="Last modified: {}".format(most_recent))
                    self.label_print.grid(row=3, column=0, rowspan=1, columnspan=3, padx=(0, 0), pady=(10, 10))

                read_db(self)
                



                


        def fileTransfer(self, custom_source, custom_destination):
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
                        conn = sqlite3.connect('file_transfer.db')
                        with conn:
                            c = conn.cursor()
                            c.execute("INSERT INTO timestamps VALUES({})".format(current_time))
                            conn.commit()
                            c.close()
                        conn.close()

                        messagebox.showinfo("File Transfer", "Files moved successfully!")
                        
                        
                            
                        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()














    
