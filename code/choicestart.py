import easygui
import subprocess
from easygui import *
msg ="System Type"
title = "ALTA E-Solutions Diagnostics"
choices = ["Desktop", "Laptop", "Workstation", "Monitor", "Cancel"]
choice = buttonbox(msg, title, choices)
if choice=="Desktop":
    subprocess.call(["sh", "/home/alta/code/dtdia.sh"])
if choice=="Laptop":
    subprocess.call(["sh", "/home/alta/code/ltdia.sh"])
if choice=="Workstation":
    subprocess.call(["sh", "/home/alta/code/wsdia.sh"])
if choice=="Monitor":
    subprocess.call(["sh", "/home/alta/code/modia.sh"])
