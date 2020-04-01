import easygui
import subprocess
from easygui import *
msg = "Select Model"
title = "Bios Flasher 1.0"
choices = ["650G1", "840G1", "840G2", "840G3", "850G1", "6560b", "6570b", "8460p", "8470p", "8570p", "9470m","Cancel"]
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
elif choice == choices[4]:
   with open(choices[4], "a+") as file_object:
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
   append_new_line(choices[4], "flashrom -p programmer -VV -l layout -i region -w filename")
elif choice == choices[5]:
   with open(choices[5], "a+") as file_object:
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
   append_new_line(choices[5], "flashrom -p programmer -VV -l layout -i region -w filename")
elif choice == choices[6]:
   with open(choices[6], "a+") as file_object:
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
   append_new_line(choices[6], "flashrom -p programmer -VV -l layout -i region -w filename")
elif choice == choices[7]:
   with open(choices[7], "a+") as file_object:
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
   append_new_line(choices[7], "flashrom -p programmer -VV -l layout -i region -w filename")
elif choice == choices[8]:
   with open(choices[8], "a+") as file_object:
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
   append_new_line(choices[8], "flashrom -p programmer -VV -l layout -i region -w filename")
elif choice == choices[9]:
   with open(choices[9], "a+") as file_object:
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
   append_new_line(choices[9], "flashrom -p programmer -VV -l layout -i region -w filename")
elif choice == choices[10]:
   with open(choices[10], "a+") as file_object:
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
   append_new_line(choices[10], "flashrom -p programmer -VV -l layout -i region -w filename")
elif choice=="Cancel":
   msg ="Where Too?"
   title = "Bios Flasher 1.0"
   choices = ["Go Back", "Quit"]
   choice = choicebox(msg, title, choices)
   if choice=="Go Back":
       subprocess.call(["python3", "first_sel.py"])
   elif choice=="Quit":
       easygui.msgbox("Goodbye")