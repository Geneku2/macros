from pynput import keyboard

p_pressed = False
r_pressed = False

def on_press(key):
    global p_pressed
    global r_pressed

    try:
        if(str(format(key.char)) == "p"):
            p_pressed = True
            print("REQUEST DETECTED, ENDING AFTER CURRENT CYCLE!!")
    except AttributeError:
        pass

    try:
        if(str(format(key.char)) == "r"):
            r_pressed = True
            print("APPLICATION READY DETECTED")
    except AttributeError:
        pass

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()