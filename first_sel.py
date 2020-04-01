import easygui
import subprocess
from easygui import *
msg = "Brand of Unit"
title = "Bios Flasher 1.0"
choices=['HP','Lenovo','Dell','Other', 'Cancel']
choice=buttonbox(msg, title,choices)
if choice=="HP":
    subprocess.call(["python3", "hp.py"])
elif choice=="Lenovo":
    subprocess.call(["python3", "lenovo.py"])
elif choice=="Dell":
    subprocess.call(["python3", "dell.py"])
elif choice=="Other":
    subprocess.call(["python3", "other.py"])
else:
    easygui.msgbox("Goodbye")
