import Entry_Box
from ..Storage import Entry_Storage
#import Shortcut_V1
from tkinter import *
from tkinter import ttk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("test program name")

arr = Entry_Storage.StorageReader("test_entry.txt")

e = Entry_Box.labelmodule(root, arr.datalist)

root.mainloop()