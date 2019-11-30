###################
##### IMPORTS #####
###################
from pynput.mouse import Button, Controller
import keyboard
import time


#####################
##### VARIABLES #####
#####################
mouse = Controller()
start_key = '+'
stop_key = '-'
status = False
macro_time = 0.01


###################
##### WELCOME #####
###################
print(" ")
print(" Python macro")
print(f" Macro wait time: {macro_time}")
print(" ")
print(" Start: +")
print(" Stop: -")
print(" ")


###########################
##### MACRO MECHANICS #####
###########################
while True:
    if status == True:
        mouse.click(Button.left)
        if keyboard.is_pressed(stop_key):
            print("(-) Macro has stopped")
            status = False
        time.sleep(macro_time)
    elif keyboard.is_pressed(start_key) and status == False:
        print("(+) Macro has started")
        status = True
    time.sleep(macro_time)
