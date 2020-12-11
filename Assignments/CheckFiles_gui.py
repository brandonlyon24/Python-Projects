#   Author:     Brandon Lyon
#
#   Purpose:    Create a script that recreates this GUI
#
#
#
import tkinter
from tkinter import *
from tkinter import filedialog

window = Tk()


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.varBrowse = StringVar()
        self.varBrowse2 = StringVar()

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Check Files')
        self.master.config(bg='lightgray')


##        self.btnBrowse = Button(self.master, text="Browse...", width=10, height=2)
##        self.btnBrowse.grid(row=1, column=0, padx=(10,40), pady=(30,0), sticky=NE)

        self.button_Browse = Button(window, text = "Browse...", command = browseFiles, width=10, height=2)
        self.btnBrowse.grid(row=1, column=0, padx=(10,40), pady=(30,0), sticky=NE)








        

        self.btnBrowse2 = Button(self.master, text="Browse...", width=10, height=2)
        self.btnBrowse2.grid(row=2, column=0, padx=(10,40), pady=(30,0), sticky=NE)

        self.txtBrowse = Entry(self.master,text=self.varBrowse, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse.grid(row=1, column=1, padx=(10,0), pady=(10,0))

        self.txtBrowse2 = Entry(self.master,text=self.varBrowse2, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse2.grid(row=2, column=1, padx=(10,0), pady=(10,0))

        self.btnCheck4 = Button(self.master, text="Check for files...", width=10, height=2)
        self.btnCheck4.grid(row=3, column=0, padx=(10,40), pady=(30,0), sticky=NW)

        self.btnClosePro = Button(self.master, text="Close Program", width=10, height=2)
        self.btnClosePro.grid(row=4, column=2, padx=(10,40), pady=(30,0), sticky=SE)

            #Define the listbox with a scrollbar and grid them
        self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
        self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
        self.lstList1.bind('<<ListboxSelect>>',lambda event: askDir_func.onSelect(self,event))
        self.scrollbar1.config(command=self.lstList1.yview)
        self.scrollbar1.grid(row=1,column=6,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
        self.lstList1.grid(row=1,column=4,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)




def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))
    




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    window.mainloop()
    
