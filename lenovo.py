import easygui
import subprocess
from easygui import *
msg = "Select Model"
title = "Bios Flasher 1.0"
choices = ["M92p", "T430", "T450", "X220","Cancel"]
choice = choicebox(msg, title, choices)
    #index choices ^          
#easygui.msgbox(choices[])
if choice == choices[0]:
   with open(choices[0], "a+") as file_object:
      file_object.seek(0)
      data = file_object.read(100)
      if len(data) > 0 :
         file_object.write("\n")
      file_object.write("#!/bin/sh")
   def append_new_line(file_name, text_to_append):
         """Append given text as a new line at the end of file"""
      #Open the file in append & read mode ('a+')
         with open(file_name, "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
               file_object.write("\n")
            file_object.write(text_to_append)
   append_new_line(choices[0], "flashrom -p programmer -VV -l layout -i region -w filename")
elif choice == choices[1]:
   with open(choices[1], "a+") as file_object:
      file_object.seek(0)
      data = file_object.read(100)
      if len(data) > 0 :
         file_object.write("\n")
      file_object.write("#!/bin/sh")
   def append_new_line(file_name, text_to_append):
         """Append given text as a new line at the end of file"""
      #Open the file in append & read mode ('a+')
         with open(file_name, "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
               file_object.write("\n")
            file_object.write(text_to_append)
   append_new_line(choices[1], "flashrom -p programmer -VV -l layout -i region -w filename")
elif choice == choices[2]:
   with open(choices[2], "a+") as file_object:
      file_object.seek(0)
      data = file_object.read(100)
      if len(data) > 0 :
         file_object.write("\n")
      file_object.write("#!/bin/sh")
   def append_new_line(file_name, text_to_append):
         """Append given text as a new line at the end of file"""
      #Open the file in append & read mode ('a+')
         with open(file_name, "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
               file_object.write("\n")
            file_object.write(text_to_append)
   append_new_line(choices[2], "flashrom -p programmer -VV -l layout -i region -w filename")
elif choice == choices[3]:
   with open(choices[3], "a+") as file_object:
      file_object.seek(0)
      data = file_object.read(100)
      if len(data) > 0 :
         file_object.write("\n")
      file_object.write("#!/bin/sh")
   def append_new_line(file_name, text_to_append):
         """Append given text as a new line at the end of file"""
      #Open the file in append & read mode ('a+')
         with open(file_name, "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
               file_object.write("\n")
            file_object.write(text_to_append)
   append_new_line(choices[3], "flashrom -p programmer -VV -l layout -i region -w filename")
elif choice=="Cancel":
   msg ="Where Too?"
   title = "Bios Flasher 1.0"
   choices = ["Go Back", "Quit"]
   choice = choicebox(msg, title, choices)
   if choice=="Go Back":
       subprocess.call(["python3", "first_sel.py"])
   elif choice=="Quit":
       easygui.msgbox("Goodbye")