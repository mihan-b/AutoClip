from re import L
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
        self.rekey_module = keyinputbox(self)
        self.rekey_module.pack()
        self.ref_GUI = basis
        self.data = [None,None]
    def callback(self):
        self.ref_GUI.update_data([self.data[0], self.textbox.get()])
    def update_text(self, KVlist):
        self.rekey_module.update_text(KVlist)
        self.textbox.delete(0,END)
        self.data = KVlist.copy()
       # self.entry_display.update_text(self.data)
        self.textbox.insert(0,self.data[1])

class info_frame(Frame):
    def __init__(self, basis):
        Frame.__init__(self,basis)
        self.L_data = StringVar()
      #  self.R_data = StringVar()
        self.Ltxt = Label(self, textvariable = self.L_data)
       # self.Rtxt = Label(self, textvariable = self.R_data)
        self.Ltxt.pack(side = LEFT)
      #  self.Rtxt.pack(side = RIGHT)
    def update_text(self, KVlist):
        self.L_data.set(KVlist[0])
       # self.R_data.set(KVlist[1])

class keyupdatebox(Toplevel):
    def __init__(self, basis):
        Toplevel.__init__(self)
        self.basis = basis
        self.textvar = StringVar()
        self.textbox = Label(self, textvariable=self.textvar)
        self.textbox.pack()
        self.offbutton = Button(self, text= "Finish combo entry", command = self.close)
        self.offbutton.pack()
    def append_term(self, newchar):
        self.textvar.set(self.textvar.get() + " " + newchar)
    def close(self):
        self.basis.update_data(tuple(self.textvar.get().split(" ")[1:]))
        self.destroy()

class keyinputbox(Frame):
    def __init__(self, basis):
        Frame.__init__(self,basis)
        self.ref_GUI = basis
        self.entry_display = info_frame(self)
        self.entry_display.pack(side = TOP)
        self.updatebutton = Button(self, text = "Change combo", command = self.callback)
        self.updatebutton.pack(side = BOTTOM)
    def callback(self):
        self.ref_GUI.ref_GUI.Combo_Edit_Flag = True
        self.update_box = keyupdatebox(basis= self)
        return
    def update_text(self, KVlist):
        self.entry_display.update_text(KVlist)
    def update_data(self, data):
        self.ref_GUI.ref_GUI.Combo_Edit_Flag = False
        self.ref_GUI.data[0] = data
        self.update_text([data,0])