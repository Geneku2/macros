from pynput import keyboard

pressed_8 = False
pressed_9 = False

def on_press(key):
    global pressed_8
    global pressed_9

    try:
        if(str(format(key.char)) == "9"):
            pressed_9 = True
            print("REQUEST DETECTED, ENDING AFTER CURRENT CYCLE!!")
    except AttributeError:
        pass

    try:
        if(str(format(key.char)) == "8"):
            pressed_8 = True
            print("APPLICATION READY DETECTED")
    except AttributeError:
        pass

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()