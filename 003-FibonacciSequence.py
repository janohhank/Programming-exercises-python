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
## Task: 003-FibonacciSequence:
## Create a program, which calculates the Fibonacci sequence elements.
##
## The program's input is a number, which defines the required n'th element.
## The output of the program is the first nth element of the Fibonacci sequence.
##
## Extra task-1: Create the Fibonacci calculation method with recursive and iterative logic too.
## Extra task-2: Change the program to calculate exactly just the n'th element of the sequence (closed-form of the expression).
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author Kishazi "janohhank" Janos

# Import argparse package for easier command line argument parsing.
import argparse
# Import math package for mathematical functions.
import math

def fibonacciRecursive(nthElement):
	if((nthElement == 0) or (nthElement == 1)):
		return nthElement
	else:
		return fibonacciRecursive(nthElement - 1) + fibonacciRecursive(nthElement - 2)

def fibonacciIterative(nthElement):
	result = 0
	previousElement = 1

	print(str(result),end=' ')
	for i in range(nthElement):
		nextElement = result + previousElement
		previousElement = result
		result = nextElement

		print(str(result),end=' ')
	print()
	return result

def fibonacciClosedForm(nthElement):
	a = pow((1.0 + math.sqrt(5.0)) / 2.0, nthElement)
	b = pow((1.0 - math.sqrt(5.0)) / 2.0, nthElement)
	result = (1.0 / math.sqrt(5.0)) * (a - b)
	return result

parser = argparse.ArgumentParser(description="002-FibonacciSequence exercise.")
parser.add_argument("--selectedNumber",required=True,type=int,help="The selected n\'th element, natural number.")

args = parser.parse_args()
selectedNumber = args.selectedNumber

if(selectedNumber < 1):
	raise Exception("The selected number must be a natural number!")

print("[" + __file__ + "]" + "[INFO]" + " The selected n\'th element number is: " + str(selectedNumber))

print("[" + __file__ + "]" + "[INFO]" + " Fibonacci sequence with recursive logic:")
for n in range(selectedNumber + 1):
	nthElement = fibonacciRecursive(n)
	print(str(nthElement),end=' ')
print()

print("[" + __file__ + "]" + "[INFO]" + " Fibonacci sequence with iterative logic:")
nthElement = fibonacciIterative(selectedNumber)

nthElement = fibonacciClosedForm(selectedNumber)
print("[" + __file__ + "]" + "[INFO]" + " The result of the closed form logic is: " + str(nthElement))