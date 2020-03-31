from easygui import *
msg = "Brand of Unit"
title = "Bios Flasher 1.0"
choices=['HP','Lenovo','Dell','Other']
choice=buttonbox(msg, title,choices)
if choice=='Physics':
    msgbox("I like physics")
elif choice=='Chemistry':
    msgbox("I like Chemistry")
elif choice=='Maths':
    msgbox("Math is fun")
elif choice=='Other':
    msgbox("Ohh thats sad! Your favourite subject is not in the list")