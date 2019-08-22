#!/usr/bin/python3

## General info:
## * The created program have to communicate in english with the user.
##  Furthermore the code variables/methods/classes etc... be named in English.
##
## * The program have to possible to handle the wrong user inputs and warnings the user how to use the program.
##
## * When you use 3rd party code from stackoverflow or other source, always reference this in the code in a comment.
##  Even if you modified the code.
##
## Task: 015-NumberGuessing
## Create a program which can randomly select a number, and add tips for the user to figure out the number.
## Firstly the program waits for two numbers from the standard input which will be an intervall. The program
## selects a number from this intervall, for example intervalls:  40-60, 0-100, 100-1000.
## After that the program select a number randomly from this intervall, use the random library:
## https://docs.python.org/2/library/random.html.
##
## And the game begins at this point, the program gets numbers from the user, and answers it:
## small, big, far smaller, far bigger. This continues until the user figure out the selected number.
##
## Extra task:
## The end of the program prints all the user guesses in chronological order.
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author Kishazi "janohhank" Janos

# Import argparse package for easier command line argument parsing.
import argparse
# This module implements pseudo-random number generators for various distributions.
import random

parser = argparse.ArgumentParser(description="015-NumberGuessing.")
parser.add_argument("--intervalLow",required=True,type=int,help="The input interval minimum value.")
parser.add_argument("--intervalHigh",required=True,type=int,help="The input interval maximum value.")

args = parser.parse_args()
intervalLow = args.intervalLow
intervalHigh = args.intervalHigh

if(intervalLow == intervalHigh):
	raise Exception("The requsted minimum and maximum interval are the same! It needs to be different.")
if(intervalLow > intervalHigh):
	raise Exception("The requsted minimum interval is higher then the maximum!")

randomNumber = int(random.uniform(intervalLow, intervalHigh))

guessesList = []
found = False
while found != True:
	try:
		number = int(input("[" + __file__ + "]" + "[INFO]" + "Take a guess: "))
	except ValueError:
		print("[" + __file__ + "]" + "[INFO]" + "You need to take an integer guess!")
		continue

	if(number == randomNumber):
		found = True
		print("[" + __file__ + "]" + "[INFO]" + "You found the magic number! " + str(number))
		continue
	elif(number < randomNumber):
		print("[" + __file__ + "]" + "[INFO]" + "The magic number is higher!")
	elif(number > randomNumber):
		print("[" + __file__ + "]" + "[INFO]" + "The magic number is smaller!")

	guessesList.append(number)

print("[" + __file__ + "]" + "[INFO]" + "Your guess list is: " + str(guessesList))