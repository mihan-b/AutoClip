# Import modules
import platform
import time
import pyautogui
import pyperclip
import keyboard
from playsound import playsound

# Lists of shortcut inputs and outputs
input_list =[
    "ac",
    "ad",
    "c",
    "d",
    "h",
    "s",
    "@"]

output_list = [
    "accessibility",
    "Advisory Committee for Persons with Disabilities",
    "committee",
    "disabilities",
    "City of Hamilton",
    "successfully",
    "Best regards,\nJames LastName\nMcMaster University\n(905)525-9140"]
#NOTE can be converted into a file

# Determines what key is used to paste
def paste_key():
    # Command for Mac
    if platform.system() == "Darwin":
        key = "command"
    # Ctrl for Windows
    else:
        key = "ctrl"
    return key

# Gets output based on input
def output_select(shortcut):
    try:
        #Gets output from index of input
        idx = input_list.index(shortcut)
        output = output_list[idx]
    except:
        #If it doesn't exist, return NA
        output = "NA"
    return output

#Copy to clipboard
def copy_to_clip(txt):
    return pyperclip.copy(txt)


#Main function
def main():
    while True:
        if keyboard.read_key() == "=":
           # playsound('/Users/mihanbandara/Downloads/notification.wav')
            print("Activated")
            #Always running
            while True:
                #User inputs shortcut key(s)
                shortcut=input()
                #Output is based on output function
                output=output_select(shortcut)
                if keyboard.read_key() == "enter":
                    #If shortcut does not exist, print that
                    if output == "NA":
                        print ("Shortcut does not exist")
                    #If shortcut does exist
                    else:
                        copy_to_clip(output)
                        #Print that the output has been copied
                        print (output, "copied to clipboard")
                        #Paste delay
                        time.sleep(3)
                        #Paste from clipboard to cursor
                        with pyautogui.hold(paste_key()):
                            pyautogui.press(['v'])
                            break
                        break

main()
