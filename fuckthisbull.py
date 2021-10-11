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

kCont = kController()


while not quit.p_pressed:
    for i in range(1516,10000):
        kCont.type(str(i))
        keyboard.press("enter")
        time.sleep(3)
    
    