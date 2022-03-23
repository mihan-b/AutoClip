import Scroll_Frame
from tkinter import *
from tkinter import ttk

class textframemodule(Frame):
    def __init__(self, basis, reference_list):
        Frame.__init__(self, basis)
        self.pack()
        self.datalist = reference_list
        self.entrylist = []
        for i in range(len(self.datalist)):
            self.entrylist.append(ttk.Label(self, text = self.datalist[i]).grid(column = i, row = 0))

class labelmodule(Scroll_Frame.VScrollFrame):
    def __init__(self, basis, reference_list):
        Scroll_Frame.VScrollFrame.__init__(self,basis)
        self.pack(padx = 5, pady = 5)
        self.datalist = reference_list
        self.frame_entry_list = []
        for i in range(len(self.datalist)):
            self.frame_entry_list.append(textframemodule(self.interior, self.datalist[i]).pack())
