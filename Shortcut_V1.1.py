import time
from threading import Thread, Timer
from pynput import keyboard
import queue
from GUI import GUI
from tkinter import *

keyboardentry = keyboard.Controller()



onstate = False 
statearr = []
statearredit = False
interchangequeue = queue.Queue(20)



root = Tk()
root.title("test program name")

e = GUI.GUI(root,"test_entry.txt")
e.pack()

#Note: we assume that a timeout doesnt lead to any output
def time_out():
    global onstate, statearr, statearredit
    onstate = False
    while(True): #wait for list to be safe to edit
        if (statearredit == False):
            statearredit = True
            statearr = [] #if timeout, reset the stored characters
            statearredit = False
            return

def statearrappend():
    global statearr, onstate, interchangequeue, statearredit
    delete_timer = None
    while(True):
        time.sleep(0.1)
        if not interchangequeue.empty():
            key = interchangequeue.get()
            if key == keyboard.Key.esc:
                print(onstate)
                onstate = not onstate
                if onstate == False:
                    print_values(e.dataset.datalist)
                    delete_timer.cancel()
                else:
                    delete_timer = Timer(5, time_out)
                continue
            if (onstate):
                while(True): #wait for list to be safe to edit
                    if (statearredit == False):
                        statearredit = True
                        statearr.append(clean_key(key))
                        print(statearr)
                        statearredit = False
                        break
                continue

def add_key_to_queue(key):
    global interchangequeue
    interchangequeue.put(key)

def clean_key(key):
    cleankey = str(key)
    if cleankey[0] == "'" :
        return cleankey[1:len(cleankey)-1]
    else:
        return cleankey.split(".")[1]

def print_values(list_dict):
    global statearr, keyboardentry, hotkeychecker
    comparator = tuple(statearr)
    print(comparator)
    statearr = []
    if comparator in list_dict:
        print(list_dict[comparator])
        hotkeychecker.stop() #kill the listener so that we dont lag out from reading our typed text
        keyboardentry.type(list_dict[comparator])
        regeneratelistener()

hotkeychecker = keyboard.Listener(on_press=add_key_to_queue)
state_arr_updater = Thread(target = statearrappend)

def regeneratelistener():
    global hotkeychecker
    hotkeychecker = keyboard.Listener(on_press=add_key_to_queue)

#adAdvisory Committee for Persons with Disabilities
hotkeychecker.start()
state_arr_updater.start()
root.mainloop()