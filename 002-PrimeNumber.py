#!/usr/bin/python

## General info:
##	* The created program have to communicate in english with the user.
##	  Furthermore the code variables/methods/classes etc... be named in English.
##
##	* The program have to possible to handle the wrong user inputs and warnings the user how to use the program.
##
##	* When you use 3rd party code from stackoverflow or other source, always reference this in the code in a comment.
##	  Even if you modified the code.
##
## Task: 001-PrimeNumber:
## Create a mini program, which tells you if a number is prime number.
##
## The program's input is the choosen number.
## The program writes the result into the standard output (for example: "This <number> is a prime number.").
##
## Extra task: Extend the program with a time measure (for example python time package). Measure the running times with different inputs.
##
## @author Kishazi "janohhank" Janos

# Import argparse package for easier command line argument parsing.
import argparse
# Import time package for time measure
import time

parser = argparse.ArgumentParser(description='002-PrimeNumber exercise.')
parser.add_argument('--selectedNumber',required=True,type=int,help='The selected natural number.')

args = parser.parse_args()
selectedNumber = args.selectedNumber

if(selectedNumber < 1):
	raise Exception("The selected number must be a natural number!")

print("[" + __file__ + "]" + "[INFO]" + " The selected number is: " + str(selectedNumber))

startTime = time.time()

# Warning range() or xrange() can be dangeorus in these situations.
# The selected number can be very large and the xrange() possibly throws a MemoryError.
dividers = 0
for i in xrange(1, selectedNumber + 1):
	if(selectedNumber % i == 0):
		dividers += 1

endTime = time.time()
elapsedTime = endTime - startTime

print("[" + __file__ + "]" + "[INFO]" + " The selected number has " + str(dividers) + " dividers.")

if(dividers == 2):
	print("[" + __file__ + "]" + "[INFO]" + " The selected number is a prime!")
else:
	print("[" + __file__ + "]" + "[INFO]" + " The selected number is not a prime!")

print("[" + __file__ + "]" + "[INFO]" + " The program counting takes " + str(elapsedTime * 1000) + " milliseconds.")
