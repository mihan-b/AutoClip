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

#note: these are not actually global variables, its only in the scope of the module, so it's not as bad practice tbh
outerframe = upperframe = namesetter = confirmbutton = database = None

def initialize(basis):
    global outerframe, upperframe, namesetter, confirmbutton
    outerframe = Frame(basis)
    upperframe = Frame(outerframe)
    namesetter = label_box(upperframe, "Phrase")
    confirmbutton = Button(upperframe, text = "save", command = data_state_update)
    outerframe.pack(padx = 5, pady = 5)
    upperframe.pack()
    namesetter.pack(side = LEFT, padx = 5, pady = 5)
    confirmbutton.pack(side = RIGHT, padx = 5, pady = 5)
     
def text_UI_update(x):
    global namesetter
    namesetter.update_text(x) #entry storage format needs revision to make data updates work via GUI


def data_state_update():
    return