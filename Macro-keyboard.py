# Copyright by Mathias Nicolajsen
# Code by Mathias Nicolajsen

# Imports
from pynput.mouse import Controller
import keyboard
import time
import os
from threading import Thread

# ASCII art for a better interface
letters = {
	"a":
	"""
   #
  # #
 #   #
#     #
#######
#     #
#     #
	""",
	"b":
	"""
######
#     #
#     #
######
#     #
#     #
######
	""",
	"c":
	"""
 #####
#     #
#
#
#
#     #
 #####
	""",
	"d":
	"""
######
#     #
#     #
#     #
#     #
#     #
######
	""",
	"e":
	"""
#######
#
#
#####
#
#
#######
	""",
	"f":
	"""
#######
#
#
#####
#
#
#
	""",
	"g":
	"""
 #####
#     #
#
#  ####
#     #
#     #
 #####
	""",
	"h":
	"""
#     #
#     #
#     #
#######
#     #
#     #
#     #
	""",
	"i":
	"""
###
 #
 #
 #
 #
 #
###
	""",
	"j":
	"""
      #
      #
      #
      #
#     #
#     #
 #####
	""",
	"k":
	"""
#    #
#   #
#  #
###
#  #
#   #
#    #
	""",
	"l":
	"""
#
#
#
#
#
#
#######
	""",
	"m":
	"""
#     #
##   ##
# # # #
#  #  #
#     #
#     #
#     #
	""",
	"n":
	"""
#     #
##    #
# #   #
#  #  #
#   # #
#    ##
#     #
	""",
	"o":
	"""
#######
#     #
#     #
#     #
#     #
#     #
#######
	""",
	"p":
	"""
######
#     #
#     #
######
#
#
#
	""",
	"q":
	"""
 #####
#     #
#     #
#     #
#   # #
#    #
 #### #
	""",
	"r":
	"""
######
#     #
#     #
######
#   #
#    #
#     #
	""",
	"s":
	"""
 #####
#     #
#
 #####
      #
#     #
 #####
	""",
	"t":
	"""
#######
   #
   #
   #
   #
   #
   #
	""",
	"u":
	"""
#     #
#     #
#     #
#     #
#     #
#     #
 #####
	""",
	"v":
	"""
#     #
#     #
#     #
#     #
 #   #
  # #
   #
	""",
	"w":
	"""
#     #
#  #  #
#  #  #
#  #  #
#  #  #
#  #  #
 ## ##
	""",
	"x":
	"""
#     #
 #   #
  # #
   #
  # #
 #   #
#     #
	""",
	"y":
	"""
#     #
 #   #
  # #
   #
   #
   #
   #
	""",
	"z":
	"""
#######
     #
    #
   #
  #
 #
#######
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
			keyboard.press_and_release(buttonKey)
			time.sleep(macro_time)
		else:
			time.sleep(0.01)

# Function for clearing the interface
def clear():
	os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# If statement, for checking if program was executed correctly
if __name__ == "__main__":

	# Introduces user to the application
	clear()
	print("\nPYTHON MACRO FOR KEYBOARD")
	print("\nPlease choose which character to use (a-z)")

	# Functions, for controlling the introduction to the application
	runStart = True
	repeat1 = False
	repeat2 = False
	while runStart:
		if repeat1:
			clear()
			print("\n###################################")
			print("Please type a valid character (a-z)")
			print("###################################")

		# Prompts the user to choose which character to use
		buttonKey = input(">>").lower()

		# Checks if the user has entered a string longer or lower than 1. Also checks if the user has entered a string and not a number
		if len(buttonKey) == 1 and isinstance(buttonKey, str) and not buttonKey.isnumeric():

			# Runs the second part, where the user has to choose how long between each keyboard press
			while runStart:
				if repeat2:
					clear()
					print("\n########################")
					print("Please type a valid time")
					print("########################")
				else:
					clear()
					print("\nPYTHON MACRO FOR KEYBOARD")
					print("\nChossen key:")
					if buttonKey in letters:
						print(letters[buttonKey])
					print("\nPlease type how long between each keyboard press (seconds)")

				# Prompts the user to choose how long between each keyboard press
				macro_time = input(">>")

				# Checks if the user has entered a integer/float
				try:
					macro_time = float(macro_time)

					# Tells user about how to use the macro
					clear()
					print("\nPYTHON MACRO FOR KEYBOARD")
					print("\nChossen key:")
					if buttonKey in letters:
						print(letters[buttonKey])
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
		else:
			repeat1 = True
