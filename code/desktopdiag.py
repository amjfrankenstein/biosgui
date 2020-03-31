import easygui
import subprocess
from easygui import *
msg = "Start Desktop Diagnostics?"
title = "Confirm"
ch=ynbox(msg, title)
if ch==0:
    subprocess.call(["sh", "/home/alta/code/chst.sh"])
else:
    msg = "Check Hard Drive Health?"
    title = "Confirm"
    ch=ynbox(msg, title)
    if ch==0:
        subprocess.call(["sh", "/home/alta/code/dtdia.sh"])
    else:
        subprocess.call(["gksu", "gsmartcontrol"])  
        msg = "Open DVD\CD\BR Tray?"
        title = "Confirm"        
        ch=ynbox(msg, title)
        if ch==0:
            subprocess.call(["sh", "/home/alta/code/dtdia.sh"])
        else:
            subprocess.call("eject") 


