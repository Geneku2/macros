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
import SKILL_farming_cropinfo as crops

mCont = mController()
kCont = kController()

print("LOADING PROCESS...")
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("LOADED! PRESS \"9\" TO CANCEL CYCLE WHEN RUNNING!!!")


front_walk_time = 0
back_walk_time = 0

mode = crops.cane()

set_ = 0
def setspawn():
        global set_
        if set_ == 0:
            #sets spawn and warps home in case of disconnect
            keyboard.press("t")
            kCont.type("/sethome")
            keyboard.press("enter")
            keyboard.press("t")
            kCont.type(mode.ret_command)
            keyboard.press("enter")
        else:
            for i in range(2):
                keyboard.press("t")
                keyboard.press("up")
                keyboard.press("up")
                keyboard.press("enter")
            if set_ > 20:
                set_ = 0
        set_ = set_ + 1

def walkingPattern():
    mCont.press(mButton.left)
    while True:
        #walks to the left, then to the right covering 2 rows, 2 timess
        for i in range(0,4):
            keyboard.keyDown(mode.front_key)
            time.sleep(mode.walk_time)
            keyboard.keyUp(mode.front_key)
            keyboard.keyDown(mode.back_key)
            time.sleep(mode.walk_time)
            keyboard.keyUp(mode.back_key)
    
        setspawn()
        mCont.press(mButton.left)

miningThread = threading.Thread(target=walkingPattern, args=(), daemon=True)
miningThread.start()

while not quit.pressed_9:
    pass
    