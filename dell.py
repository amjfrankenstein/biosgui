import easygui
import subprocess
from easygui import *
msg = "Select Model"
title = "Bios Flasher 1.0"
choices = ["Cancel"]
choice = choicebox(msg, title, choices)
    #index choices ^          
#easygui.msgbox(choices[])
if choice=="Cancel":
   msg ="Where Too?"
   title = "Bios Flasher 1.0"
   choices = ["Go Back", "Quit"]
   choice = choicebox(msg, title, choices)
   if choice=="Go Back":
       subprocess.call(["python3", "first_sel.py"])
   elif choice=="Quit":
       easygui.msgbox("Goodbye")