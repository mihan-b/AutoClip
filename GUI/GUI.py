from Storage import Entry_Storage
#import Shortcut_V1
from tkinter import *
from tkinter import ttk
from GUI import Entry_Box, rename_box

class GUI(Frame):
    def __init__(self, basis, filename):
        Frame.__init__(self,basis)
        self.dataset = Entry_Storage.StorageReader(filename)
        self.labelmodule = Entry_Box.labelmodule(self,self.dataset)
        self.renamemodule = rename_box.label_box(self,"Enter Text")
        self.labelmodule.pack()
        self.renamemodule.pack(side = BOTTOM)
    def text_UI_update(self, KVpair):
        self.renamemodule.update_text(KVpair)
    def update_data(self, KVpair):
        self.dataset.modify_list(KVpair[0],KVpair[1])
        self.labelmodule.dataframe.textupdate(KVpair[0],KVpair[1], keychange = False)
        print(self.dataset.datalist)
        print(self.labelmodule.keyframe.full_list)