#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Import modules
import platform 
import pyperclip
import pyautogui
import time
   

#List of shortcut inputs
#NOTE can be converted to file
input_list=[
    "ac",
    "ad",
    "c",
    "d",
    "s",
    "@"]

#List of shortcut ouputs
#NOTE can be converted to file
output_list=[
    "accessibility",
    "Advisory Committee for Persons with Disabilities",
    "committee",
    "disabilities",
    "successfully",
    "Best regards,\nJames LastName\nMcMaster University\n(905)525-9140"]

#Determines what key is used to paste
def paste_key():
    #Command for Mac
    if platform.system()=="Darwin":
        key = "command"
    #Ctrl for Windows
    else:
        key = "ctrl"
    return key

#Gets output based on input
def output_select(shortcut):
    try:
        #Gets output from index of input
        idx = input_list.index(shortcut)
        output = output_list[idx]
    except: 
        #If it doesn't exist, return NA
        output = "NA"
    return output

def copy_to_clip(txt):
    #Copy to clipboard
    return pyperclip.copy(txt)

def main():
    #Always running
    while True:
        #User inputs shortcut key(s)
        shortcut=input()
        #Output is based on output function
        output=output_select(shortcut)
        #If shortcut does not exist, print that
        if output == "NA":
            print ("Shortcut does not exist")
        #If shortcut does exist
        else:
            copy_to_clip(output)
            #Print that the output has been copied
            print (output, "copied to clipboard")
            #Paste delay
            time.sleep(10)
            #Paste from clipboard to cursor
            with pyautogui.hold(paste_key()):
                pyautogui.press(['v'])

main()


# In[ ]:


