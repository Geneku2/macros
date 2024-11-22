from pynput import keyboard

print("READY: (8)\nQUIT: (9)")

READY_PRESSED = False
QUIT_PRESSED = False

def on_press(key):
    global READY_PRESSED
    global QUIT_PRESSED

    try:
        if(str(format(key.char)) == "9"):
            QUIT_PRESSED = True
            print("<ending after current cycle>")
    except AttributeError:
        pass

    try:
        if(str(format(key.char)) == "8"):
            READY_PRESSED = True
            print("<starting>")
    except AttributeError:
        pass

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()