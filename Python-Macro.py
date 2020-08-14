# Copyright by Mathias Nicolajsen
# Code by Mathias Nicolajsen

from pynput.mouse import Button, Controller
import keyboard
import time

# Variables
mouse = Controller()
start_key = '+'
stop_key = '-'
status = False

# Asks if user wants to use left or right click as macro
print("\nWould you like to use right or left click as macro? (right/left)\n")
msg = input(">>").lower()

# Checks what the user said
if msg == "right" or msg == "r":
    buttonUse = Button.right
elif msg == "left" or msg == "l":
    buttonUser = Button.left
else:
    raise Exception("You can only use right or left")

# Asks user how many seconds there should be between each click
print("\n\nHow much time should there be between each click? (0.01)\n")
macro_time = float(input(">>"))

# Tells user about how to use the macro
print("\n\n\nMacro wait time: {0}\n".format(macro_time))
print("Start: +")
print("Stop: -")
print("\nExit: del key")

# Run the macro program
while True:
    if status == True:
        mouse.click(Button.left)
        if keyboard.is_pressed(stop_key):
            print("(-) Macro has stopped")
            status = False
    elif keyboard.is_pressed(start_key) and status == False:
        print("(+) Macro has started")
        status = True
    elif keyboard.is_pressed("del"):
        print("(X) Stopping program")
        break

    time.sleep(macro_time)  # Delay
