from Storage import Entry_Storage
#import Shortcut_V1
from tkinter import *
from tkinter import ttk
from GUI import Entry_Box, rename_box

class GUI(Frame):
    def __init__(self, basis, filename):
        Frame.__init__(self,basis)
        self.dataset = Entry_Storage.StorageReader(filename)
        self.labelmodule = Entry_Box.labelmodule(self,self.dataset)