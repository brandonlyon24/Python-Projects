#
#   Author: Brandon Lyon
#
#
#
#
#
import webbrowser
import tkinter
import tkinter as tk
from tkinter import *
import Body_func

f = open("websitebuilder.html", "w")


f.close()




class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        Body_func.center_window(self,500,300)
        self.master.title("Website Builder")
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        # load in the GUI widgets from a separate module, 
        load_gui(self)






def load_gui(self):
    self.lbl_body = tk.Label(self.master,text='Text Added Here will be added to the Body of a website:')
    self.lbl_body.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)



    self.txt_body = tk.Entry(self.master,text='')
    self.txt_body.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)



    self.btn_add = tk.Button(self.master,width=12,height=2,text='Add',command=lambda: Body_func.addToList(self))
    self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
