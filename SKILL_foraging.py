# mouse controlling
from pynput.mouse import Button as mButton
from pynput.mouse import Controller as mController

#keyboard controlling
from pynput.keyboard import Key as kButton
from pynput.keyboard import Controller as kController
import pydirectinput as keyboard

# feeback and listening
from pynput import mouse

# time managing and controlled actions
import time

#shitty position processing i made
import positionProcessing as pospro
import threading

mCont = mController()
kCont = kController()

#warps the player to the hub
def warphub():
    keyboard.press("t")
    kCont.type("/warp hub")
    time.sleep(1)
    keyboard.press("enter")

#warps the player to the home
def warphome():
    keyboard.press("t")
    kCont.type("/warp home")
    time.sleep(1)
    keyboard.press("enter")

#simple method for placing and breaking with optimized time
def placeAndBreak():
    #place tree
    keyboard.press("3")
    time.sleep(0.1)
    mCont.click(mButton.right, 1)
    time.sleep(0.1)
    
    #bone tree
    keyboard.press("2")
    time.sleep(0.1)
    mCont.press(mButton.right)
    time.sleep(1)
    mCont.release(mButton.right)

    #test break in case boning error
    mCont.click(mButton.left, 1)
    time.sleep(0.1)
    #break tree

    keyboard.press("1")
    time.sleep(0.1)
    mCont.press(mButton.left)
    time.sleep(0.4)
    mCont.release(mButton.left)
    time.sleep(0.1)


#clicks stuff funct for clicking thing rep times
def repClick(times,delay):
    for i in range(0,times):
        mCont.click(mButton.left, 1)
        time.sleep(delay)

def goToBuilder():

    CHECKPOINT = (-10.5,-46.5,-49,-30)
    SAFETY = 6.0
    #LEFT OUT OF MAP
    while pospro.getCoords()[0] > CHECKPOINT[0]:
        keyboard.keyDown("a")
        if abs(CHECKPOINT[0] - pospro.getCoords()[0]) < SAFETY:
            keyboard.keyDown("alt")
    keyboard.keyUp("a")
    keyboard.keyUp("alt")

    #BACK TO BUILDER ALLEY
    while pospro.getCoords()[2] < CHECKPOINT[1]:
        keyboard.keyDown("s")
        if abs(CHECKPOINT[1] - pospro.getCoords()[2]) < SAFETY:
            keyboard.keyDown("alt")
    keyboard.keyUp("s")
    keyboard.keyUp("alt")

    print("CP3")
    #LEFT TO BUILDER DOOR
    a = pospro.getCoords()[0]
    while a > CHECKPOINT[2]:
        #FUCK IMAGE RECOGNITION
        if(pospro.getCoords()[0] < -200):
            print("a")
            a = pospro.getCoords()[0]/10
        elif(pospro.getCoords()[0] <= -90):
            print("b")
            a = pospro.getCoords()[0]+50
        else:
            a = pospro.getCoords()[0]
        print("A: " + str(a) + "  P: " + str(pospro.getCoords()[0]))
        keyboard.keyDown("a")
        if abs(CHECKPOINT[2] - a) < SAFETY:
            keyboard.keyDown("alt")
    print("LAST: " + str(a))
    keyboard.keyUp("a")
    keyboard.keyUp("alt")

    print("CP4")
    while pospro.getCoords()[2] < CHECKPOINT[3]:
        print(pospro.getCoords()[2])
        keyboard.keyDown("s")
        if abs(CHECKPOINT[3] - pospro.getCoords()[2]) < SAFETY:
            keyboard.keyDown("alt")
    keyboard.keyUp("s")
    keyboard.keyUp("alt")

doImageToString = threading.Thread(target=pospro.loopedImToString, args=(), daemon=True)
doImageToString.start()

time.sleep(3)

goToBuilder()

#cont.position = (cont.position[0], 5)

#looks down after, technically irrelevant after discovering obi system
def __lookdown():
    for i in range(0,10):
        mCont.move(0,30)
        time.sleep(0.025)