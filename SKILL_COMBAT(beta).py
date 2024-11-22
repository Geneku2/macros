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

def walkingPattern():
    while True:
        #sets spawn and warps home in case of disconnect
        keyboard.keyDown("s")

        #restarts process every 3 minutes in case some shit happens
        time.sleep(180)
        keyboard.keyUp("s")

mCont = mController()
kCont = kController()

miningThread = threading.Thread(target=walkingPattern, args=(), daemon=True)
miningThread.start()

while not quit.QUIT_PRESSED:
    mCont.move(-10,0)
    time.sleep(0.1);
    