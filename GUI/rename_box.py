from tkinter import *
from tkinter import ttk

class label_box(Frame):
    def __init__(self, basis, name):
        Frame.__init__(self,basis)
        self.header = Label(self, text=f'{name}')
        self.header.pack(side =LEFT, padx = 5)
        self.textbox = Entry(self)
        self.textbox.pack(side =RIGHT)
    def get(self):
        return self.textbox.get()
    def update_text(self, data):
        self.textbox.delete(0,END)
        self.textbox.insert(0,data)

