import easygui
import subprocess
from easygui import *
msg = "Start Laptop Diagnostics?"
title = "Confirm"
ch=ynbox(msg, title)
if ch==0:
    subprocess.call(["sh", "/home/alta/code/chst.sh"])
else:
    msg = "Begin Screen Colour Test?"
    title = "Confirm"
    ch=ynbox(msg, title)
    if ch==0:
        subprocess.call(["sh", "/home/alta/code/ltdia.sh"])
    else:
        subprocess.call(['feh', '/home/alta/Pictures/ScreenTest/', '*', '-x', '-F', '-Y', '--zoom', 'fill'])
        msg = "Begin Keyboard Test?"
        title = "Confirm"
        ch=ynbox(msg, title)
        if ch==0:
            subprocess.call(["sh", "/home/alta/code/ltdia.sh"])
        else:
            subprocess.call(['chromium-browser', '--fast', '--window-size=1069,416', '--app=file:///home/alta/Documents/key/key/tester.html'])
            msg = "Begin Speaker Test?"
            title = "Confirm"
            ch=ynbox(msg, title)
            if ch==0:
                subprocess.call(["sh", "/home/alta/code/ltdia.sh"])               
            else:
                subprocess.call(['lxterminal', '-e', 'speaker-test', '-t', 'wav', '-c', '2'])
                msg = "Begin Microphone Test?"
                title = "Confirm"
                ch=ynbox(msg, title)
                if ch==0:
                    subprocess.call(["sh", "/home/alta/code/ltdia.sh"])    
                else:                        
                    subprocess.call(['lxterminal', '-e', 'arecord', '-vvv', '-f', 'dat', '/dev/null'])
                    msg = "Begin WebCam Test?"
                    title = "Confirm"
                    ch=ynbox(msg, title)
                    if ch==0:
                        subprocess.call(["sh", "/home/alta/code/ltdia.sh"])    
                    else:  
                        subprocess.call(['cheese'])   
                        msg = "Check Battery Health?"
                        title = "Confirm"
                        ch=ynbox(msg, title)
                        if ch==0:
                            subprocess.call(["sh", "/home/alta/code/ltdia.sh"]) 
                        else:
                            subprocess.call(["xfce4-power-manager-settings"])
                            msg = "Check Hard Drive Health?"
                            title = "Confirm"
                            ch=ynbox(msg, title)
                            if ch==0:
                                subprocess.call(["sh", "/home/alta/code/ltdia.sh"])
                            else:
                                subprocess.call(["gksu", "gsmartcontrol"])   


