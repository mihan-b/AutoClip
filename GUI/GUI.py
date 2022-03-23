import Entry_Box
#import Shortcut_V1
from tkinter import *
from tkinter import ttk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("test program name")

arr = []
for i in range(0, 50, 2):
    arr.append[f'entry: {i}', f'entry: {i+1}']

e = Entry_Box.labelmodule(root, arr)

root.mainloop()