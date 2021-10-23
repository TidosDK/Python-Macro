# Copyright by Mathias Nicolajsen
# Code by Mathias Nicolajsen

# Imports
from pynput.mouse import Button, Controller
import keyboard
import time
import os
from threading import Thread

# ASCII art for a better interface
mouse_ASCII = {
	"l":
	"""
         ||
         ||
.---------.--------.
| ####### |        |
| ####### |        |
| ####### |        |
|---------'--------|
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
`                  '
 `.              ,'
   \_          _/
     '-,____,-'
	""",
	"r":
	"""
         ||
         ||
.---------.--------.
|         | ###### |
|         | ###### |
|         | ###### |
|---------'--------|
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
`                  '
 `.              ,'
   \_          _/
     '-,____,-'
	"""
}

# Variables
mouse = Controller()
start_key = '+'
stop_key = '-'
status = False
runProgram = True

# Function for checking for input
def check_for_input():
	global status
	global runProgram

	while runProgram:
		if status == True and keyboard.is_pressed(stop_key):
			print("(-) Macro has stopped")
			status = False

		elif status == False and keyboard.is_pressed(start_key):
			print("(+) Macro has started")
			status = True

		elif keyboard.is_pressed("del"):
			print("(X) Stopping program")
			runProgram = False
		time.sleep(0.01)

# Function for running the macro
def macro():
	global status
	global runProgram

	while runProgram:
		if status:
			mouse.click(buttonUse)
			time.sleep(macro_time)
		else:
			time.sleep(0.01)

# Function for clearing the interface
def clear():
	os.system('cls' if os.name in ('nt', 'dos') else 'clear')

if __name__ == "__main__":

	# Introduces user to the application
	clear()
	print("\nPYTHON MACRO FOR MOUSE")
	print("\nPlease choose: left or right")

	# Functions, for controlling the introduction to the application
	runStart = True
	repeat1 = False
	repeat2 = False
	while runStart:
		if repeat1:
			clear()
			print("\n############################")
			print("Please choose: left or right")
			print("############################")

		# Prompts the user to choose between left or right
		msg = input(">>").lower()
		repeat1 = False

		# Checks if the user has entered a string and not a number
		if isinstance(msg, str) and not msg.isnumeric():
			if msg == "l" or msg == "left":
				msg = "l"
				buttonUse = Button.left
			elif msg == "r" or msg == "right":
				msg = "r"
				buttonUse = Button.right
			else:
				repeat1 = True

		if repeat1 == False:
			while runStart:
					# Asks user how many seconds there should be between each click
					if repeat2:
						clear()
						print("\n########################")
						print("Please type a valid time")
						print("########################")
					else:
						clear()
						print("\nPYTHON MACRO FOR MOUSE")
						print("\nChossen key:")
						if msg in mouse_ASCII:
							print(mouse_ASCII[msg])
						print("\nPlease type how long between each keyboard press (seconds)")

					# Prompts the user to choose how long between each keyboard press
					macro_time = input(">>")

					# Checks if the user has entered a integer/float
					try:
						macro_time = float(macro_time)

						# Tells user about how to use the macro
						clear()
						print("\nPYTHON MACRO FOR MOUSE")
						print("\nChossen key:")
						if msg in mouse_ASCII:
							print(mouse_ASCII[msg])
						print("\nChossen time: {0} seconds".format(macro_time))
						print("\nStart key: +")
						print("Stop key: -")
						print("Exit program: del")

						# Ends the while loops, because the user has given enough information
						runStart = False

						# Starts threading
						Thread(target=check_for_input).start()
						Thread(target=macro).start()

					except:
						repeat2 = True
