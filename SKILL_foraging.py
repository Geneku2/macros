# mouse controlling
from pynput.mouse import Button as mButton
from pynput.mouse import Controller as mController

#keyboard controlling
from pynput.keyboard import Key
from pynput.keyboard import Controller as kController
import pydirectinput as keyboard

# quit
import quitListener as quit

# time managing and controlled actions
from time import sleep

#shitty position processing i made
import threading

mCont = mController()
kCont = kController()

_troubleshoot = False

_preset_tree_coords = True
builder_coords = (-1547,357)
green_coords = (-1193,452)
tree_coords = (-1381, 457)
stack_coords = (-1109,460)

_preset_bone_coords = True
combat_coords = (-1634,462)
bone1_coords = (-1369,368)
bone2_coords = (-1462,460)
buy_coords = (-1555,462)
ammount_coords = (-1004,463)
done_coords = (-1274,1014)
exec_coords = (-1279,447)

_preset_craft_coords = True
table_coords = (-1278, 546)
meal_coords = (-1018, 457)

def move_to_pos(position):
    mCont.move(position[0]-mCont.position[0],position[1]-mCont.position[1])

def buy_saplings():
    #call phone
    keyboard.press("4")
    mCont.click(mButton.right, 1)
    sleep(0.3)

    #open builder
    move_to_pos(builder_coords)
    sleep(0.3)
    mCont.click(mButton.left, 1)
    sleep(5.5)

    #open green thumb
    move_to_pos(green_coords)
    sleep(0.3)
    mCont.click(mButton.left, 1)
    sleep(0.3)

    #click sapling
    move_to_pos(tree_coords)
    sleep(0.3)
    mCont.click(mButton.right, 1)
    sleep(0.3)

    #click stack
    move_to_pos(stack_coords)
    sleep(0.3)
    mCont.click(mButton.left, 1)
    sleep(0.3)
    kCont.press(Key.esc)

def buy_bones():
    keyboard.press("t")
    sleep(0.3)
    kCont.type("/bz")
    sleep(0.3)
    kCont.press(Key.enter)
    sleep(0.3)

    move_to_pos(combat_coords)
    sleep(0.3)
    mCont.click(mButton.left, 1)
    sleep(0.3)

    move_to_pos(bone1_coords)
    sleep(0.3)
    mCont.click(mButton.left, 1)
    sleep(0.3)

    move_to_pos(bone2_coords)
    sleep(0.3)
    mCont.click(mButton.left, 1)
    sleep(0.3)

    move_to_pos(buy_coords)
    sleep(0.3)
    mCont.click(mButton.left, 1)
    sleep(0.3)

    move_to_pos(ammount_coords)
    sleep(0.3)
    mCont.click(mButton.left, 1)
    sleep(0.3)
    kCont.type("21")
    sleep(0.75)

    move_to_pos(done_coords)
    sleep(0.3)
    mCont.click(mButton.left, 1)
    sleep(0.3)

    move_to_pos(exec_coords)
    sleep(0.3)
    mCont.click(mButton.left, 1)
    sleep(0.3)
    kCont.press(Key.esc)

def craft_bones():
    keyboard.press("q")
    sleep(0.3)
    mCont.click(mButton.left, 1)
    sleep(0.3)
    move_to_pos(table_coords)
    sleep(0.3)
    mCont.click(mButton.left, 1)
    sleep(0.3)
    move_to_pos(meal_coords)
    sleep(0.3)
    mCont.click(mButton.left, 1)
    sleep(0.3)
    with kCont.pressed(Key.shift_l):
        mCont.click(mButton.left, 1)
    sleep(0.3)
    kCont.press(Key.esc)

if(not _preset_tree_coords):
    print("Hover Mouse Over Builder and Press Enter:")
    input()
    builder_coords = mCont.position

    print("Hover Mouse Over Green Thumb and Press Enter:")
    input()
    green_coords = mCont.position

    print("Hover Mouse Over Oak Sapling and Press Enter:")
    input()
    tree_coords = mCont.position

    print("Hover Mouse Over Stack and Press Enter:")
    input()
    stack_coords = mCont.position

if(not _preset_bone_coords):
    print("Hover Mouse Over Combat and Press Enter:")
    input()
    combat_coords = mCont.position

    print("Hover Mouse Over Bones and Press Enter:")
    input()
    bones1_coords = mCont.position

    print("Hover Mouse Over Bones and Press Enter:")
    input()
    bones2_coords = mCont.position

    print("Hover Mouse Over Buy and Press Enter:")
    input()
    buy_coords = mCont.position

    print("Hover Mouse Over Amount and Press Enter:")
    input()
    ammount_coords = mCont.position

    print("Hover Mouse Over Done and Press Enter:")
    input()
    done_coords = mCont.position

    print("Hover Mouse Over Execute and Press Enter:")
    input()
    exec_coords = mCont.position

if(not _preset_craft_coords):
    print("Hover Mouse Over Crafting Table and Press Enter:")
    input()
    table_coords = mCont.position

    print("Hover Mouse Over Execute and Press Enter:")
    input()
    meal_coords = mCont.position

while _troubleshoot:
    input()
    print(mCont.position)

def do_foraging():
    while True:
        buy_saplings()
        buy_bones()
        craft_bones()

        for i in range(15):
            kCont.release("a")
            keyboard.press("2")
            sleep(0.3)
            mCont.click(mButton.right, 1)
            sleep(0.3)
            mCont.click(mButton.right, 1)
            sleep(0.3)
            kCont.press("d")
            sleep(0.2)
            kCont.release("d")
            mCont.click(mButton.right, 1)
            sleep(0.3)
            mCont.click(mButton.right, 1)
            kCont.press("a")
            sleep(0.3)

            keyboard.press("3")
            mCont.press(mButton.right)
            sleep(3)
            mCont.release(mButton.right)
            
            keyboard.press("1")
            mCont.press(mButton.left)
            sleep(0.5)
            mCont.release(mButton.left)
        with kCont.pressed(Key.ctrl_l):
            keyboard.press("2")
            sleep(0.3)
            keyboard.press("v")
            sleep(0.3)
            keyboard.press("3")
            sleep(0.3)
            keyboard.press("v")
            sleep(0.3)
            keyboard.press("t")
            sleep(0.3)
        kCont.type("/is")
        sleep(0.3)
        kCont.press(Key.enter)
        sleep(0.3)


print("LOADING PROCESS...")
print(3)
sleep(1)
print(2)
sleep(1)
print(1)
sleep(1)
print("LOADED! PRESS \"9\" TO CANCEL CYCLE WHEN RUNNING!!!")

miningThread = threading.Thread(target=do_foraging, args=(), daemon=True)
miningThread.start()

while not quit.pressed_9:
    pass