#!/usr/bin/python3
from tkinter import *
import os
import sys

help = '''
pynote <option> 

<--------------------------------------->
	-d : open file with directory 
	-b : open Base file Data 
	-h : open help menu

'''
path = "data"
arg = sys.argv
root = Tk()
file =None

quit = False

def autosave(event):
   file = open(path, "w")
   s = text.get("1.0", "end")
   file.write(s)



try:
    if arg[1] == "-b":
        path="/usr/local/bin/data"
    elif arg[1] == "-d":
        path = arg[2]
    elif arg[1] == "-h":
        print(help)
        quit = True
except:
    pass

try:
    if quit == False:
       file = open(path, "r")
       print(path)
except:
    try:
    	if quit == False:
           file = open(path, "w")
           os.chmod(path, 0o777)
    except:
        print("please run with permission")
root.title("pynote")
root.geometry("720x480")

scroll = Scrollbar(root, bg="#485460",troughcolor="#808e9b",width=10,elementborderwidth=0)
scroll.pack(side=RIGHT, fill=Y)


text= Text(root,bg='#F9E79F', fg="#17202A", font=("Verdana", 14))
text.bind("<KeyPress>", autosave)
text.focus_set()
text.pack(fill=Y)

scroll.config(command=text.yview)
text.config(width=root.winfo_screenwidth()-20,height=root.winfo_screenheight(),yscrollcommand=scroll.set)

if quit == True:
    root.destroy()
    root.quit() 
try:
    text.insert(END,file.read())
except:
    try:
        f=open(path,"r")
    except:
        root.destroy()
        root.quit()

root.mainloop()


