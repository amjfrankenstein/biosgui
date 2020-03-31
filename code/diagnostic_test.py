import easygui
import subprocess
from easygui import *
msg = "Start ALTA Diagnostics?"
title = "Confirm"
ch=ynbox(msg, title)
if ch==0:
    exit(0)
else:
    msg = "Begin Screen Colour Test?"
    title = "Confirm"
    ch=ynbox(msg, title)
    if ch==0:
        exit(0)
    else:
        subprocess.call(['feh', '/home/alta/Pictures/ScreenTest/', '*', '-x', '-F', '-Y', '--zoom', 'fill'])
        msg = "Did Colour Test Succeed? "
        title = "Confirm"
        ch=ynbox(msg, title)
        if ch==0:
            exit(0)
        else:
            msg = "Begin Keyboard Test?"
            title = "Confirm"
            ch=ynbox(msg, title)
            if ch==0:
                exit(0)
            else:
                subprocess.call(['chromium-browser', '--fast', '--window-size=1069,416', '--app=file:///home/alta/Documents/key/key/tester.html'])
                msg = "Did Keyboard Test Succeed? "
                title = "Confirm"
                ch=ynbox(msg, title)
                if ch==0:
                    exit(0)
                else:
                    msg = "Begin Speaker Test?"
                    title = "Confirm"
                    ch=ynbox(msg, title)
                    if ch==0:
                        exit(0)               
                    else:
                        subprocess.call(['lxterminal', '-e', 'speaker-test', '-t', 'wav', '-c', '2'])
                        msg = "Did Speaker Test Succeed? "
                        title = "Confirm"
                        ch=ynbox(msg, title)
                        if ch==0:
                            exit(0)
                        else:
                            msg = "Begin Microphone Test?"
                            title = "Confirm"
                            ch=ynbox(msg, title)
                            if ch==0:
                                exit(0)    
                            else:                        
                                subprocess.call(['lxterminal', '-e', 'arecord', '-vvv', '-f', 'dat', '/dev/null'])
                                msg = "Did Microphone Test Succeed? "
                                title = "Confirm"
                                ch=ynbox(msg, title)
                                if ch==0:
                                    exit(0)
                                else:
                                    msg = "Begin WebCam Test?"
                                    title = "Confirm"
                                    ch=ynbox(msg, title)
                                    if ch==0:
                                        exit(0)    
                                    else:  
                                        subprocess.call(['cheese'])   
                                        msg = "Did WebCam Test Succeed? "
                                        title = "Confirm"
                                        ch=ynbox(msg, title)
                                        if ch==0:
                                            exit(0)
                                        else:
                                            msg = "Check Battery Health?"
                                            title = "Confirm"
                                            ch=ynbox(msg, title)
                                            if ch==0:
                                                exit(0) 
                                            else:
                                                subprocess.call(["xfce4-power-manager-settings"])
                                                msg = "Check Hard Drive Health?"
                                                title = "Confirm"
                                                ch=ynbox(msg, title)
                                                if ch==0:
                                                    exit(0)
                                                else:
                                                    subprocess.call(["gksu", "gsmartcontrol"])   


