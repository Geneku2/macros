#DONE AT -0.0 / -2.5

# mouse controlling
from pynput.mouse import Button as mButton
from pynput.mouse import Controller as mController

# keyboard controlling
from pynput.keyboard import Key as kButton
from pynput.keyboard import Controller as kController
import pydirectinput as keyboard

# feeback and listening
from pynput import mouse

# time managing and controlled actions
import time

# escape listener
import quitListener as quit

import threading

mCont = mController()
kCont = kController()

def resetPos():
    keyboard.keyDown("a")
    time.sleep(4.9)
    keyboard.keyUp("a")

def mine():
    drill = True

    times = (0.33,0.41,0.45,0.46,0.42,0.44,0.44)

    for i in range(0,len(times)):
        keyboard.keyDown("d")
        time.sleep(times[i])
        keyboard.keyUp("d")
        time.sleep(1.25 if drill else 1.4)

def mainPart():
    while True:
        resetPos() #set to default posdition
        mine()

print("LOADING...")
macro = threading.Thread(target=mainPart, args=(), daemon=True)
time.sleep(3)

print("LOADED! PRESS \"l\" TO CANCEL CYCLE WHEN RUNNING!!!")

keyboard.keyDown("alt") #perma-sneak
mCont.press(mButton.left) #perma-mine
macro.start()

while not quit.quit_pressed:
    time.sleep(1)

keyboard.keyUp("d")
keyboard.keyUp("a")
keyboard.keyUp("alt")
keyboard.keyUp("d")
keyboard.keyUp("a")
mCont.release(mButton.left)
print("CYCLE ENDED")


