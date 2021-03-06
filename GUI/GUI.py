from Storage import Entry_Storage
#import Shortcut_V1
from tkinter import *
from tkinter import ttk
from GUI import Entry_Box, rename_box

class GUI(Frame):
    def __init__(self, basis, filename, key):
        Frame.__init__(self,basis)
        self.Combo_Edit_Flag = False
        self.dataset = Entry_Storage.StorageReader(filename, key)
        self.labelmodule = Entry_Box.labelmodule(self,self.dataset)
        self.renamemodule = rename_box.label_box(self,"Enter Text")
        self.labelmodule.pack(padx = 10, pady = 10)
        self.renamemodule.pack(side = BOTTOM, pady= 15)
        self.soundtogglestate = True
        self.root = basis
    def text_UI_update(self, KVpair):
        self.renamemodule.update_text(KVpair)
    def update_data(self, KVpair):
        self.labelmodule.data_update(KVpair)
        self.dataset.modify_list(KVpair[0],KVpair[1])
