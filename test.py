from pynput.keyboard import Controller as kC
from time import sleep

k = kC()
sleep(5)
print("gogogo")
k.tap("a")
k.press("d")
sleep(5)
k.release("d")