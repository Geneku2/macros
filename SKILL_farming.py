# mouse controlling
from pynput.mouse import Button as mButton
from pynput.mouse import Controller as mController

# keyboard controlling
import pydirectinput as keyboard
from pynput.keyboard import Controller as kController

# time managing and threading
import time
from datetime import datetime
import threading

# escape listener
import quitListener as quit

print("LOADING PROCESS...")
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("LOADED! PRESS \"l\" TO CANCEL CYCLE WHEN RUNNING!!!")

def walkingPattern():
    while True:
        #walks to the left, then to the right covering 2 rows, 2 times
        for i in range(0,2):
            mCont.press(mButton.left)
            keyboard.keyDown("d")
            time.sleep(20)
            keyboard.keyUp("d")
            mCont.press(mButton.left)
            keyboard.keyDown("a")
            time.sleep(20)
            keyboard.keyUp("a")

        #sets spawn and warps home in case of disconnect
        keyboard.press("t")
        kCont.type("/sethome")
        keyboard.press("enter")
        keyboard.press("t")
        kCont.type("/is")
        keyboard.press("enter")

mCont = mController()
kCont = kController()

miningThread = threading.Thread(target=walkingPattern, args=(), daemon=True)
miningThread.start()

while not quit.p_pressed:
    pass
    