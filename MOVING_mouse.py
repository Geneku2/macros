#fancy computer vision shit
import threading

#mouse movement
from pynput.mouse import Button as mButton
from pynput.mouse import Controller as mController

import time


import positionProcessing as pospro


doImageToString = threading.Thread(target=pospro.loopedImToString, args=(), daemon=True)
doImageToString.start()

ddd = 90

a = ddd/10 if (ddd > 100) else ddd-50 if (ddd >= 90) else ddd

print(a)

time.sleep(2)
while True:
    print("Coordinates: " + str(pospro.__strProcessCoords("AYZ: -13.280 / 70.00000 / -45.198-~.)")))
    time.sleep(0.5)
    


