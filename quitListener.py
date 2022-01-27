from pynput import keyboard

quit_pressed = False

def on_press(key):
    global quit_pressed

    try:
        if(str(format(key.char)) == "l"):
            quit_pressed = True
            print("REQUEST DETECTED, ENDING AFTER CURRENT CYCLE!!")
    except AttributeError:
        pass

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()