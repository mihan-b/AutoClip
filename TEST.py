from GUI import GUI
#import Shortcut_V1
from tkinter import *
from tkinter import ttk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("test program name")

e = GUI.GUI(root,"test_entry.txt")
e.pack()

root.mainloop()
