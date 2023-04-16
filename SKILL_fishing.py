#sound detection
import pyaudio
import wave

# mouse controlling
from pynput.mouse import Button as mButton
from pynput.mouse import Controller as mController

# keyboard controlling
import pydirectinput as keyboard

# time managing and threading
import time
from datetime import datetime
import threading

# escape listener
import quitListener as quit
#------------------------------------------------------------

mCont = mController()
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = (r"C:\Users\Shyryyuu\Downloads\output.wav")

p = pyaudio.PyAudio()

dev_index = -1
#Index: 0 | Name: Microsoft Sound Mapper - Input , hostAPI: 0  | uhhh, idk yet
#Index: 1 | Name: Microphone Array (Intel® Smart  , hostAPI: 0 | System Mic
#Index: 2 | Name: Stereo Mix (Realtek(R) Audio) , hostAPI: 0   | System Sound
#Index: 3 | Name: Microsoft Sound Mapper - Output , hostAPI: 0 | Output thats bugged
#Index: 4 | Name: Speakers (Realtek(R) Audio) , hostAPI: 0     | Output thats bugged

#Gets the device on the computer that is responsible for channeling system sound
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if (dev['hostApi'] > 0):
        break
    print("Index: " + str(i) + " | Name: " + dev["name"] + " , hostAPI: " + str(dev['hostApi']) + " , Max Channels: " + str(dev['maxInputChannels']))
    #Sound Channel is required to be the StereoMix with API 0
    if (dev['name'] == 'Stereo Mix (Realtek(R) Audio)' and dev['hostApi'] == 0):
        dev_index = dev['index']

print("FOUND " + p.get_device_info_by_index(dev_index)['name'] + " at index " + str(dev_index))
print('------------------------------------------------------')

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=dev_index
                )

print("LOADING PROCESS...")
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("LOADED! PRESS \"9\" TO CANCEL CYCLE WHEN RUNNING!!!")
#frames = []

silence = True

#the recording part   
def getSoundStream():
    global stream
    global CHUNK
    global silence

    while True:
        data = stream.read(CHUNK)
        #frames.append(data)

        #Part for determining if there is sound playing or not
        indicatorCount = 0
        for character in str(data):
            if character.isnumeric() and int(character) > 4:
                indicatorCount = indicatorCount + 1
            if indicatorCount > 50: #50 is an objective number but it works most of the time
                silence = False
                break
        #print(silence, indicatorCount)

def antiAFK():
    while True:
        keyboard.keyDown("alt") #sneak
        keyboard.keyDown("a")
        keyboard.keyUp("a")
        keyboard.keyDown("d")
        keyboard.keyUp("d")

        then = datetime.now()
        while (datetime.now() - then).total_seconds() < 0.1:
            mCont.move(0,-1)
            time.sleep(0.01)

        then = datetime.now()
        while (datetime.now() - then).total_seconds() < 0.6:
            mCont.move(0,1)
            time.sleep(0.01)

        time.sleep(1)

streamRecThread = threading.Thread(target=getSoundStream, args=(), daemon=True)
streamRecThread.start()

antiAFKThread = threading.Thread(target=antiAFK, args=(), daemon=True)

print("Waiting for User to Boot Application - Press \"8\" When Ready to Run")
while not quit.pressed_8:
    time.sleep(1)

antiAFKThread.start()
keyboard.press("3")
mCont.click(mButton.right, 1)
while not quit.pressed_9:
    if not silence:
        mCont.click(mButton.right, 1)
        time.sleep(0.1)
        keyboard.press("2")
        mCont.click(mButton.right, 1)
        time.sleep(0.1)
        keyboard.press("3")
        time.sleep(0.1)
        mCont.click(mButton.right, 1)
        time.sleep(3.7)
        silence = True

print("CYCLE ENDED")

keyboard.keyUp("a")
keyboard.keyUp("d")
keyboard.keyUp("alt")
keyboard.keyUp("a")
keyboard.keyUp("d")
keyboard.keyUp("alt")