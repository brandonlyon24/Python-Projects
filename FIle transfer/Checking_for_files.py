import tkinter
from tkinter import *
from tkinter import filedialog


def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)
window = Tk()
window.title('Check Files')
window.geometry("500x500")
window.config(background = "lightgray")

label_file_explorer = Label(window,  
                            text = "Check current files", 
                            width = 100, height = 4,  
                            fg = "blue") 
   
       
button_explore = Button(window, text = "Browse...", command = browseFiles)
button_explore2 = Button(window, text = "Browse...", command = browseFiles)
   
button_exit = Button(window,  
                     text = "Exit", 
                     command = exit)


label_file_explorer.grid(column = 0, row = 1, padx=(10,10), pady=(10,10), sticky=NW) 
   
button_explore.grid(column = 0, row = 2, padx=(10,10), pady=(10,10), sticky=NW)

button_explore2.grid(column = 0, row = 3, padx=(10,10), pady=(10,10), sticky=NW)
   
button_exit.grid(column = 0,row = 4, padx=(10,10), pady=(10,10), sticky=NW) 
   
# Let the window wait for any events 
window.mainloop() 
