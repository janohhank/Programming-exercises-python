##!/usr/bin/python

## General info:
##	* The created program have to communicate in english with the user.
##	  Furthermore the code variables/methods/classes etc... be named in English.
##
##	* The program have to possible to handle the wrong user inputs and warnings the user how to use the program.
##
##	* When you use 3rd party code from stackoverflow or other source, always reference this in the code in a comment.
##	  Even if you modified the code.
##
## Task: 001-QuadraticEquation:
## Create a mini program, which can calculates a predefined quadratic equation.
##
## The program's inputs are the ax^2 + bx + c = 0 equation [a,b,c] coefficents.
##
## Warning: the 'a' input can't be zero!
## Warning: the equation possibly has complex root!
##
## Extra task: Show the equation in a figure with matplotlib.
##
## Not complex test input: 6x^2 + 11x - 35 = 0
## Complex test input: 1x^2 + 2x + 3 = 0
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author Kishazi "janohhank" Janos

# Import math package for mathematical operations (cmath is for complex numbers).
import cmath
# Import numpy for scientific computing with Python.
import numpy
# Import argparse package for easier command line argument parsing.
import argparse
# Import matplotlib package for mathematical plotting.
import matplotlib.pyplot

parser = argparse.ArgumentParser(description="001-QuadraticEquation exercise.")
parser.add_argument("--a",required=True,type=int,help="The ax^2+bx+c=0 equation \'a\' coefficent, it can\'t be zero!")
parser.add_argument("--b",required=True,type=int,help="The ax^2+bx+c=0 equation \'b\' coefficent.")
parser.add_argument("--c",required=True,type=int,help="The ax^2+bx+c=0 equation \'c\' coefficent.")

args = parser.parse_args()
a = args.a
b = args.b
c = args.c

if(a == 0):
	raise Exception("The \'a\' coefficent can't be zero!")

print("[" + __file__ + "]" + "[INFO]" + " Got the following parameters, a: " + str(a) + " b: " + str(b) + " c: " + str(c))

discriminant = pow(b,2) - (4 * a * c)
x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

print("[" + __file__ + "]" + "[INFO]" + " Calculated results, x1 : " + str(x1) + " x2: " + str(x2))

if((x1.imag == 0.0) and (x2.imag == 0.0)):
	print("[" + __file__ + "]" + "[INFO]" + " Plotting the quadratic equation.")

	xRangeMin = min(x1.real,x2.real) - 10
	xRangeMax = max(x1.real,x2.real) + 10
	steps = xRangeMax - xRangeMin

	x = numpy.linspace(xRangeMin, xRangeMax, steps)
	y = a * (x**2) + x*b + c
	matplotlib.pyplot.plot(x,y,label="Quadratic curve")
	matplotlib.pyplot.plot([x1.real,x2.real],[0,0],'ro',label="Roots")
	matplotlib.pyplot.title("Quadratic equation curve")
	matplotlib.pyplot.xlabel("x axis")
	matplotlib.pyplot.ylabel("y axis")
	matplotlib.pyplot.legend()
	matplotlib.pyplot.grid()
	matplotlib.pyplot.show()
else:
	print("[" + __file__ + "]" + "[INFO]" + " This program can't visalize the complex roots results.")