# mouse controlling
from pynput.mouse import Button as mButton
from pynput.mouse import Controller as mController

# keyboard controlling
import pydirectinput as keyboard

# time managing and threading
import time
import threading

# escape listener
import quitListener as quit

def doGolemHat():
    while True:
        keyboard.keyUp("w")
        keyboard.keyUp("s")
        keyboard.keyUp("alt")
        keyboard.keyDown("alt")
        time.sleep(5.25)

#------------------------------------------------------------

mCont = mController()

golemHat = str(input("Golem Hat On (y)? ")) == "y"
print("LOADING...")
time.sleep(3)
print("LOADED! PRESS \"p\" TO CANCEL CYCLE WHEN RUNNING!!!")

if golemHat:
    hat = threading.Thread(target=doGolemHat, args=(), daemon=True)
    hat.start()

keyboard.keyDown("alt") #sneak

#actual anti-afk stuff
while not quit.p_pressed:
    keyboard.keyDown("w")
    keyboard.keyUp("w")
    keyboard.keyDown("s")
    keyboard.keyUp("s")

    for i in range(0,8):
        mCont.move(0,-1)
        time.sleep(0.01)

    for i in range(0,8):
        mCont.move(0,1)
        time.sleep(0.01)

    time.sleep(1.5)

keyboard.keyUp("alt")
print("CYCLE ENDED")