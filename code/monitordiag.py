import easygui
import subprocess
from easygui import *
msg = "Start Monitor Diagnostic?"
title = "Confirm"
ch=ynbox(msg, title)
if ch==0:
    subprocess.call(["sh", "/home/alta/code/chst.sh"])
else:
    subprocess.call(['feh', '/home/alta/Pictures/ScreenTest/', '*', '-x', '-F', '-Y', '--zoom', 'fill'])

