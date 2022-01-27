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
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("LOADED! PRESS \"L\" TO CANCEL CYCLE WHEN RUNNING!!!")

if golemHat:
    hat = threading.Thread(target=doGolemHat, args=(), daemon=True)
    hat.start()

#keyboard.keyDown("alt") #sneak

#actual anti-afk stuff
while not quit.quit_pressed:
    keyboard.keyDown("alt")
    keyboard.keyDown("w")
    time.sleep(0.125)
    keyboard.keyUp("w")
    keyboard.keyUp("alt")

    keyboard.keyDown("s")

    for i in range(0,20):
        mCont.move(0,-1)
        time.sleep(0.01)

    for i in range(0,20):
        mCont.move(0,1)
        time.sleep(0.01)

    time.sleep(1.5)
    keyboard.keyUp("s")
   #keyboard.keyDown("alt")

keyboard.keyUp("alt")
print("CYCLE ENDED")