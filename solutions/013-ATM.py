#!/usr/bin/python3

## General info:
##	* The created program have to communicate in english with the user.
##	  Furthermore the code variables/methods/classes etc... be named in English.
##
##	* The program have to possible to handle the wrong user inputs and warnings the user how to use the program.
##
##	* When you use 3rd party code from stackoverflow or other source, always reference this in the code in a comment.
##	  Even if you modified the code.
##
## Task: 013-ATM
## Write an algorithm which can calculate the change of a an ATM transaction.
## The program gets a number from the standard input and the output is the least return banknote and cash.
## The currency is hungarian forint.
##
## For example 2245 = 2000 + 200 + 2x20 + 5
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author Kishazi "janohhank" Janos

# Import argparse package for easier command line argument parsing.
import argparse

parser = argparse.ArgumentParser(description="013-ATM.")
parser.add_argument("--inputNumber",required=True,type=int,help="The input number of the ATM.")

args = parser.parse_args()
inputNumber = args.inputNumber

print("[" + __file__ + "]" + "[INFO]" + " Choosed input number is: " + str(inputNumber))

units = [10000,5000,2000,1000,500,200,100,50,20,10,5]

resultMap = {}
for unit in units:
	if(inputNumber < unit):
		continue

	result = inputNumber % unit
	resultMap[str(unit)] = int((inputNumber - result) / unit)
	inputNumber = result

print("[" + __file__ + "]" + "[INFO]" + " The ATM result map is: " + str(resultMap))