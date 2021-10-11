# conclusion for ya boi: python is shit for game making, other better software exists, please use that
# unless your making a visual novel of course, then go for it
# mnk bg

from pynput import mouse

mouseX = -99
mouseY = -99
leftClick = False
rightClick = False

# on move is easier to deal with but then again, I can just use on position
def __on_move(x, y):
    global mouseX
    global mouseY
    
    mouseX = x
    mouseY = y


# mouse button detection with python is kinda wack and I don't feel like working it out
def __on_click(x, y, button, pressed):
    global leftClick
    global rightClick

    leftClick = (str(button) == "Button.left" and pressed)
    rightClick = (str(button) == "Button.right" and pressed)

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=__on_move,
    on_click=__on_click
)
listener.start()