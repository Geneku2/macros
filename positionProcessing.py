import threading
import time

#fancy computer vision shit
import numpy as np
import pytesseract
import cv2
from PIL import ImageGrab

rawStrings = ("a","b")

def getCoords():
    try:
        return __strProcessCoords(rawStrings[0])    
    except:
        print("ERROR: COORDINATES NOT LOADED - LOADED(" + rawStrings[0] +")")

def getRotation():
    try:
        return __strProcessRot(rawStrings[1])
    except:
        print("ERROR: COORDINATES NOT LOADED - LOADED(" + rawStrings[1] +")")
        return(-180,0)

def loopedImToString():
    while True:
        __imToString()

#rotation image to string
def __imToString():
    global rawStrings
  
    # Path of tesseract executables
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
    
    textcolor = 221

    # ImageGrab-To capture the screen image in a loop; Bbox used to capture a specific area.
    rot = ImageGrab.grab(bbox =(0,463,1121,503))
    rot.save('C:/Users/Shyryyuu/Downloads/rot.png',"PNG")
    #mcfs 714,458,1066,503 are rot for direction

    #cv2.cvtColor(np.array(cap), cv2.COLOR_BGR2GRAY) returns a greyed version of the image of np.array(cap)

    rotProcessed = __isolateText(np.array(rot), 221)

    # Converted the image to monochrome for it to be easily 
    # read by the OCR and obtained the output String.
    rotstr = pytesseract.image_to_string(rotProcessed, lang ='eng')

    coords = ImageGrab.grab(bbox =(0,346,778,393))

    coords.save('C:/Users/Shyryyuu/Downloads/coords.png',"PNG")

    coordsProcessed = __isolateText(np.array(coords), 221)

    coordstr = pytesseract.image_to_string(coordsProcessed, lang ='eng')

    rawStrings = (coordstr,rotstr)

#HELPER---------------------------------------------------------------------

#makes all greytext of color textcolor to black and background to white
def __isolateText(npImageArray,textcolor):
    for i in range(0,npImageArray.shape[0]):
        for j in range(0,npImageArray[i].shape[0]):
                temp = npImageArray[i][j] == [textcolor,textcolor,textcolor]
                        
                if temp.any():
                        npImageArray[i][j] = [255,255,255]
                else:
                        npImageArray[i][j] = [0,0,0]

    return npImageArray

#processes that rotation numbers to get a tuple
def __strProcessRot(str):
    #Recorrects for common mistakes found while converting
    for x in range(0,len(str)):
        if str[x:x+1] == "O" or str[x:x+1] == "@":
            str = str[:x] + "0" + str[x+1:]
        elif str[x:x+1] == "C" or str[x:x+1] == "€":
            str = str[:x] + "(" + str[x+1:]
        elif str[x:x+1] == ",":
            str = str[:x] + "." + str[x+1:]
        elif str[x:x+1] == "i":
            str = str[:x] + "1" + str[x+1:]
        elif str[x-2:x+1] == " 07":
            str = str[:x-2] + " (7" + str[x+1:]

    paranthesisPos1 = 0
    paranthesisPos2 = len(str)

    #finds the last "(" that is usable
    for x in range(0,len(str)):
        if str[len(str)-1-x:len(str)-x] == "(":
            paranthesisPos1 = len(str)-1-x
            break
    #finds the last ")" that is usable
    for x in range(0,len(str)):
        if str[len(str)-1-x:len(str)-x] == ")":
            paranthesisPos2 = len(str)-1-x
            break
    
    rotOrientation = []
    
    str = str[paranthesisPos1 + 1:paranthesisPos2]

    for x in range(0,len(str)):
        if str[x:x+1] == " ":
            try:
                rotOrientation.append(float(str[0:x]))
                rotOrientation.append(float(str[x+3:]))
            except:
                print("Error: " + str[0:x] + " or " + str[x+3:] + " are not strings!")
            break

    return (rotOrientation[0],rotOrientation[1])

def __strProcessCoords(strg):
    #gets rids of the ♀
    strg= strg[:len(strg)-2]

    #gets rid of the XYZ: part at the beginning because its cringe
    for x in range(0,len(strg)):
        if strg[x:x+1] == " ":
            strg = strg[x + 1:]
            break

    #common errors and shit
    x = 0
    while x < len(strg):
        #print("Char " + str(x) + ": " +  strg[x:x+1])
        if strg[x:x+1] == "O" or strg[x:x+1] == "@":
            strg = strg[:x] + "0" + strg[x+1:]
        elif strg[x:x+1] == "C":
            strg = strg[:x] + "(" + strg[x+1:]
        elif strg[x:x+1] == ",":
            strg = strg[:x] + "." + strg[x+1:]
        elif strg[x:x+1] == ";" or strg[x:x+1] == "#" or strg[x:x+1] == "!":
            strg = strg[:x] + ":" + strg[x+1:]
        elif strg[x:x+1] == "—":
            strg = strg[:x] + "-" + strg[x+1:]
        elif strg[x:x+1] == "S" or strg[x:x+1] == "s":
            strg = strg[:x] + "5" + strg[x+1:]
        elif strg[x:x+1] == "“":
            strg = strg[:x] + "/" + strg[x+1:]
        elif strg[x:x+1] == " ":
            strg = strg[:x] + strg[x+1:]
            x = x - 1

        if (strg[x-1:x+1] == ".."):
            strg = strg[:x-1] + "." + strg[x+1:]
            x = x - 1
        elif (strg[x-1:x+1] == "--"):
            strg = strg[:x-1] + "-" + strg[x+1:]
            x = x - 1
        elif (strg[x-1:x+1] == "D5"):
            strg = strg[:x-1] + "5" + strg[x+1:]
            x = x - 1
        elif (strg[x-1:x+1] == "//"):
            strg = strg[:x-1] + "/" + strg[x+1:]
            x = x - 1
        
        x = x + 1
        
        
    
    #processes "/" into duple-able numbers
    parenthesisPos = []
    for x in range(0,len(strg)):
        if strg[x:x+1] == "/":
            parenthesisPos.append(x)

    return (float(strg[:parenthesisPos[0]]),float(strg[parenthesisPos[0]+1:parenthesisPos[1]]),float(strg[parenthesisPos[1]+1:]))