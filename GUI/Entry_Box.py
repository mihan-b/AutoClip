from GUI import Scroll_Frame, rename_box
from tkinter import *
from tkinter import ttk

class Bbutton(Button):
    def __init__(self, basis, txt, anchor_dir, x_pos):
        Button.__init__(self,basis, text = txt, anchor = anchor_dir, command = self.callback)
        self.x_pos = x_pos
    def callback(self): #fuck callbacks all my homies hate callbacks
        rename_box.text_UI_update(self.x_pos)

class Vframe(Frame):
    def __init__(self, basis, reference_list, index):
        Frame.__init__(self,basis)
        self.Vref = []
        self.Vlist = []
        self.index = index
        self.update(reference_list)
    def update(self,reference_list):
        for x in range(len(reference_list)):
            self.Vref.append(reference_list[x][self.index])
            self.Vlist.append(Bbutton(self, self.Vref[len(self.Vref)-1], W, x))
            self.Vlist[len(self.Vlist)-1].pack(fill = X)

class labelmodule(Scroll_Frame.VScrollFrame):
    def __init__(self, basis, reference_list):
        Scroll_Frame.VScrollFrame.__init__(self,basis)
        self.pack()
        self.datalist = reference_list
        #self.InnerFrame = Frame(self.interior).pack()
        self.Vframe_list = []
        for x in range(len(self.datalist[0])):
            self.Vframe_list.append(Vframe(self.interior, self.datalist, x))
            self.Vframe_list[len(self.Vframe_list)-1].pack(side = RIGHT)