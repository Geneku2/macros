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

def mineCobble():
    while True:
        keyboard.keyDown("s")
        #keyboard.keyDown("alt")
        #keyboard.keyUp("alt")

        oldtime = datetime.now()

        while(datetime.now() - oldtime).total_seconds() < 1200: #was 1200
            mCont.press(mButton.left)
            time.sleep(60)
            
            
        keyboard.keyUp("s")
        mCont.release(mButton.left)

        keyboard.press("t")
        kCont.type("/warp hub")
        keyboard.press("enter")
        time.sleep(10)

        keyboard.keyDown("s")
        time.sleep(7)
        keyboard.keyUp("s")
        time.sleep(3)

mCont = mController()
kCont = kController()

miningThread = threading.Thread(target=mineCobble, args=(), daemon=True)
miningThread.start()

while not quit.quit_pressed:
    pass
    