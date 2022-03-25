import time
from threading import Thread, Timer
from pynput import keyboard
import queue
from GUI import GUI
from tkinter import *

keyboardentry = keyboard.Controller() #keyboard entry instance

onstate = False #combo reading activation state
statearr = [] #list of characters for combo
statearredit = False #if statearr is being edited
interchangequeue = queue.Queue(20) #multi-thread accessable queue for buffering key presses
UI_on = True #variable to check if the UI is open

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
    while(UI_on):
        time.sleep(0.1) 
        if not interchangequeue.empty(): #if there are terms in the key reading queue yet to be processed
            key = interchangequeue.get()
            if str(key) == "'='": #if key is activation key
                print(onstate)
                onstate = not onstate
                if onstate == False: #if we were reading the key combo before this press
                    print_values(e.dataset.datalist) 
                    delete_timer.cancel() #cancels the 5 sec timer as we finished the statement
                else:
                    delete_timer = Timer(5, time_out) #starts up timer, which calls time_out after 5 sec
                continue #continue to prevent counting the activation key in the list holding the key combo
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
    interchangequeue.put(key) #add key to buffer, this is done to minimize processing time inside the key press reading thread to reduce lag

def clean_key(key):
    cleankey = str(key)
    if cleankey[0] == "'" : #when you cast a char key datatype to string, the output string has its own quotation marks. This checks for that
        return cleankey[1:len(cleankey)-1]
    else: #if the key datatype cannot describe the key as a char (i.e escape), its formatted as key.(name of the button) instead
        return cleankey.split(".")[1]

def print_values(list_dict):
    global statearr, keyboardentry, hotkeychecker
    comparator = tuple(statearr) #cast to tuple because dictionary must have tuple keys
    print(comparator)
    statearr = []
    if comparator in list_dict:
        print(list_dict[comparator])
        hotkeychecker.stop() #kill the listener so that we dont fill up interchangequeue and lag the typing out while waiting for stateappend to process all the keys
        keyboardentry.type("\b"*(len(comparator)+2) + list_dict[comparator]) #press backspace enough times to delete the shortcut, and the activation keys, then type the text
        regeneratelistener() #unkill the listener so we can read other entries

hotkeychecker = keyboard.Listener(on_press=add_key_to_queue)
state_arr_updater = Thread(target = statearrappend)

def regeneratelistener():
    global hotkeychecker
    hotkeychecker = keyboard.Listener(on_press=add_key_to_queue)
    hotkeychecker.start()

hotkeychecker.start()
state_arr_updater.start()

def exit_function():
    global root, hotkeychecker, UI_on
    hotkeychecker.stop()
    UI_on = False
    root.destroy()

root.protocol('WM_DELETE_WINDOW', exit_function)

root.mainloop()