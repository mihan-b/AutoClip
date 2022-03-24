from GUI import Scroll_Frame, rename_box
from tkinter import *
from tkinter import ttk

class Bbutton(Button):
    def __init__(self, basis, txt, anchor_dir, key, dataref):
        output = None
        print(txt)
        if len(txt) > 15:
            output = txt[0:15] + "..."
        Button.__init__(self,basis, text = output, anchor = anchor_dir, command = self.callback)
        self.key = key
        self.dataref = dataref
    def callback(self): #fuck callbacks all my homies hate callbacks
        self.dataref.text_UI_update(self.key)

class Vframe(Frame):
    def __init__(self, basis, reference_list, dataref):
        Frame.__init__(self,basis)
        self.pack(LEFT)
        self.dataref = dataref
        self.reflist = reference_list
        self.button_list = {}
        self.update()
    def update(self):
        for term in self.reflist:
            self.button_list[term] = Bbutton(self, term, S, self.dataref.datalist.keys(), self.dataref)
            self.button_list[term].pack()

class labelmodule(Scroll_Frame.VScrollFrame):
    def __init__(self, basis, dataref):
        Scroll_Frame.VScrollFrame.__init__(self,basis)
        self.dataref = dataref
        self.pack()
        self.keyframe = Vframe(self, dataref.datalist.keys(), self.dataref)
        self.dataframe = Vframe(self, dataref.datalist.values(), self.dataref)