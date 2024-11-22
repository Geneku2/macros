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
print("LOADED!")

def mineCobble():
    while True:
        mCont.press(mButton.left)
        keyboard.keyDown("s")
        
        time.sleep(1200)
        keyboard.keyUp("s")
        mCont.release(mButton.left)

        keyboard.press("t")
        kCont.type("/hub")
        keyboard.press("enter")
        time.sleep(7.5)
        keyboard.press("t")
        kCont.type("/is")
        keyboard.press("enter")
        time.sleep(7.5)

mCont = mController()
kCont = kController()

miningThread = threading.Thread(target=mineCobble, args=(), daemon=True)
miningThread.start()

while not quit.QUIT_PRESSED:
    pass
    