import mouseListener
import time

print("start")

i = 0


while True:
    print("-------------------------------------------")
    print("X: " + str(mouseListener.mouseX))
    print("Y: " + str(mouseListener.mouseY))
    print("L: " + str(mouseListener.leftClick))
    print("R: " + str(mouseListener.rightClick))
    time.sleep(1)
