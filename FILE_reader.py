
import webbrowser
import tkinter as tk
from tkinter import *
import shutil
import os,time

"""
datetime.now()
os.listdir
a loop:
    path.join or concatenate for the absoule paths to your files 

fromtimestamp

 .endswith()
 %I for hours
 %p for am/pm


 

source = '/Users/lyonb/Desktop/Created Or Modified/'

import shutil, sys, time, os
import tkinter as tk
from tkinter import *

from tkinter import filedialog
root = Tk()

def fileMove():
    sourcePath = '/Users/lyonb/Desktop/*'
    sourcePath = filedialog.askdirectory()
    receivePath = filedialog.askdirectory()
    source = sourcePath
    dest = receivePath
    files = os.listdir(source) 

    now = time.time()
    for f in files:
        src = (source) +f
        dst = (dest) +f
        if os.stat(src).st_mtime > now - 1 * 86400:
            if os.path.isfile(src):
                shutil.move(src, dst)
                print("File move is Alright, Alright, Alright")





def button_press():
    if one:
        x = 1
        display.configure(text=x)
        if two:
            x = 2
            display.configure(text=x)
            if three:
                x = 3
                display.configure(text=x)

display = LabelFrame(root, bg="red", width="462", height="60")
display.pack()


three = Button(root, text="3", width="15", height="5",command=fileMove)
three.pack(side="left")

root.mainloop()
"""


now=dt.datetime.now()
ago=now-dt.timedelta(minutes=1440)
passover=[]
for root,dirs,files in os.walk('SourceFolder'):
    for fname in files:
        path=os.path.join(root,fname)
        st=os.stat(path)
        mtime=dt.datetime.fromtimestamp(st.st_mtime)
        if mtime>ago:
            passover.append(path)







