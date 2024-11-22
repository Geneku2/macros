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

mCont = mController()
kCont = kController()

def resetPos():
    keyboard.keyDown("a")
    time.sleep(4.8)
    keyboard.keyUp("a")

def mine():
    times = (0.21,0.24,0.31,0.27,0.29,0.27,0.27)

    for i in range(0,len(times)):
        keyboard.keyDown("d")
        time.sleep(times[i])
        keyboard.keyUp("d")
        time.sleep(2.5)

print("LOADING...")

time.sleep(3)

print("LOADED! PRESS \"`\" TO CANCEL CYCLE WHEN RUNNING!!!")

keyboard.keyDown("alt") #perma-sneak
mCont.press(mButton.left) #perma-mine

while not quit.QUIT_PRESSED:
    resetPos() #set to default posdition
    mine()

mCont.release(mButton.left)
time.sleep(0.2)
keyboard.keyUp("alt")
print("CYCLE ENDED")


