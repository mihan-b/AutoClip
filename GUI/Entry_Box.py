from GUI import Scroll_Frame, rename_box
from tkinter import *
from tkinter import ttk

class Bbutton(Button):
    def __init__(self, basis, txt, anchor_dir, KVpair, ref_GUI, output_restrict):
        self.output_restrict = output_restrict
        self.Stext = StringVar()
        self.update_text(txt, KVpair)
        Button.__init__(self, basis, textvariable = self.Stext, anchor = anchor_dir, command = self.callback)
        self.KVpair = KVpair
        self.ref_GUI = ref_GUI
    def callback(self): #fuck callbacks all my homies hate callbacks
        self.ref_GUI.text_UI_update(self.KVpair)
    def update_text(self, value, KV): #shortens text to length limit, and updates
        self.KVpair = KV
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
        self.iskey = iskey
        for key, value in self.full_list.items():
            if (iskey):
                self.button_list[key] = Bbutton(self, key, S, [key, value], self.ref_GUI, output_restrict=False)
            else: #BELOW: note that the value key might need to be replaced with the original key values for access in the future
                self.button_list[key] = Bbutton(self, value, S, [key, value], self.ref_GUI, output_restrict=True) 
            self.button_list[key].pack(side= BOTTOM, fill= X)
    def updatekey(self,data):
        for k, v in self.full_list.items():
            if data[1] == v:
                self.button_list[tuple(k)].update_text(data[0],data)
    def updatevalue(self,data):
        self.button_list[tuple(data[0])].update_text(data[1],data)
    def append_term(self,data):
        self.button_list[data[0]] = Bbutton(self, data[0], S, data, self.ref_GUI, output_restrict=not self.iskey)
        self.button_list[data[0]].pack(side= BOTTOM, fill= X)
class labelmodule(Scroll_Frame.VScrollFrame):
    def __init__(self, basis, dataref):
        Scroll_Frame.VScrollFrame.__init__(self,basis)
        self.ref_GUI = basis
        self.dataref = dataref
        self.keyframe = Vframe(self.interior, dataref.datalist, self.ref_GUI, iskey = True)
        self.dataframe = Vframe(self.interior, dataref.datalist, self.ref_GUI, iskey = False, )
        self.keyframe.pack(side = LEFT)
        self.dataframe.pack(side= LEFT)
    def data_update(self, datachange):
        is_existing_key = tuple(datachange[0]) in self.dataref.datalist.keys()
        is_existing_value = datachange[1] in self.dataref.datalist.values()
        if is_existing_key:
            self.dataframe.updatevalue(datachange)
        elif is_existing_value:
            self.keyframe.updatekey(datachange)
        else:
            self.keyframe.append_term()
            self.dataframe.append_term()