from GUI import Scroll_Frame, rename_box
from tkinter import *
from tkinter import ttk

class Bbutton(Button):
    def __init__(self, basis, txt, anchor_dir, KVpair, ref_GUI, output_restrict):
        self.output_restrict = output_restrict
        self.Stext = StringVar()
        self.update_text(txt)
        Button.__init__(self, basis, textvariable = self.Stext, anchor = anchor_dir, command = self.callback)
        self.KVpair = KVpair
        self.ref_GUI = ref_GUI
    def callback(self): #fuck callbacks all my homies hate callbacks
        self.ref_GUI.text_UI_update(self.KVpair)
    def update_text(self, value): #shortens text to length limit, and updates
        if len(str(value)) > 20 and self.output_restrict:
            self.Stext.set(str(value)[0:20] + "...")
        else:
            self.Stext.set(str(value))

class Vframe(Frame):
    def __init__(self, basis, full_list, ref_GUI, iskey):
        Frame.__init__(self,basis)
        self.ref_GUI = ref_GUI
        self.full_list = full_list
        self.button_list = {}
        for key, value in self.full_list.items():
            if (iskey):
                self.button_list[key] = Bbutton(self, key, S, [key, value], self.ref_GUI, output_restrict=False)
            else: #BELOW: note that the value key might need to be replaced with the original key values for access in the future
                self.button_list[key] = Bbutton(self, value, S, [key, value], self.ref_GUI, output_restrict=True) 
            self.button_list[key].pack(side= BOTTOM, fill= X)
    def textupdate(self, key, value, keychange): #TBA: get key switch
        self.button_list[key].update_text(value)

class labelmodule(Scroll_Frame.VScrollFrame):
    def __init__(self, basis, dataref):
        Scroll_Frame.VScrollFrame.__init__(self,basis)
        self.ref_GUI = basis
        self.keyframe = Vframe(self.interior, dataref.datalist, self.ref_GUI, iskey = True)
        self.dataframe = Vframe(self.interior, dataref.datalist, self.ref_GUI, iskey = False, )
        self.keyframe.pack(side = LEFT)
        self.dataframe.pack(side= LEFT)