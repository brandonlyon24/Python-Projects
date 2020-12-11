



import os
from tkinter import *
import tkinter as tk
import sqlite3

import websitebuilder
import webbrowser

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo




def addToList(self):
    var_body = self.txt_body.get()
    
    var_body = ("""<html>
    <body>
        <p>{}</p>
    </body>
</html>""".format(var_body)) 
    print("{}".format(var_body))
    f = open("websitebuilder.html", "w")
    f.write("{}".format(var_body))
    f.close
    webbrowser.open_new_tab("websitebuilder.html")
  
    

    
            
         

        
