from tkinter import *
from tkinter import ttk

class label_box(Frame):
    def __init__(self, basis, name):
        Frame.__init__(self,basis)
        self.topframe = Frame(self)
        self.topframe.pack(side = TOP)
        self.header = Label(self.topframe, text=f'{name}')
        self.header.pack(side =LEFT, padx = 5)
        self.textbox = Entry(self)
        self.textbox.pack(side =BOTTOM)
        self.updatebutton = Button(self.topframe, text = "Save", command=self.callback)
        self.updatebutton.pack(side =RIGHT)
        self.ref_GUI = basis
    def callback(self):
        self.ref_GUI.update_data([self.data[0], self.textbox.get()])
    def update_text(self, KVlist):
        self.textbox.delete(0,END)
        self.data = KVlist
        self.textbox.insert(0,self.data[1])

