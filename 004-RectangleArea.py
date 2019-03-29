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
## Task: 004-RectangleArea:
## Creates a program which reads a specific file and interpret the contained data.
##
## This specific file is pre-generated text file and contains coordinates from rectangle corners in a 2D space.
## In the file these rectangle coordinates are in separate rows. Each row contains 4 corner coordinates (X,Y).
## First corner is the rectangle upper left corner, and the other corners are in clockwise order.
##
## Coordinate system:
##	  x axis
## (0,0)---------->
## |
## |
## | y axis
## |
## |
## v
##
## For example:
## UpperLeftCornerX,UpperLeftCornerY,UpperRigthCornerX,UpperRigthCornerY,LowerRightCornerX,LowerRightCornerY,LowerLeftCornerX,LowerLeftCornerY
##
## The task is to create a program which reads all rectangles and calculates the areas of these.
## In the end, the program writes the 3 largest rectangles calculated area values in the standard output.
##
## The program input requirements is the path of the pre-generated file.
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author Kishazi "janohhank" Janos

# This module provides a portable way of using operating system dependent functionality.
import os
# Import argparse package for easier command line argument parsing.
import argparse

parser = argparse.ArgumentParser(description="004-RectangleArea.")
parser.add_argument("--inputFilePath",required=True,type=str,help="Pre-generated input file path which contains the 2D coordinates.")

args = parser.parse_args()
inputFilePath = args.inputFilePath

if(os.path.isfile(inputFilePath) is False):
	raise Exception("The input parameter does not denote a file: " + inputFilePath)

print("[" + __file__ + "]" + "[INFO]" + " Selected pre-generated input file path: " + inputFilePath)

areas = []
with open(inputFilePath) as inputFile:
	lines = inputFile.read().splitlines()

	for line in lines:
		splitLine = str(line).split(',')
		if(len(splitLine) != 8):
			# This line doesn't contains 8 comma separated coordinates
			continue
		# lrx - ulx
		currentWidth = float(splitLine[4]) - float(splitLine[0])
		# lry - uly
		currentHeight = float(splitLine[5]) - float(splitLine[1])
		# area of the rectangle
		area = currentWidth * currentHeight

		areas.append(area)
		if(len(areas) > 3):
			list.sort(areas, reverse=True)
			del areas[-1]

resultSize = len(areas)
if(resultSize == 0):
	print("[" + __file__ + "]" + "[WARNING]" + " There are no calculable rectangles in the pre-generated file!")
elif(resultSize < 3):
	print("[" + __file__ + "]" + "[WARNING]" + " There are less then three calculable rectangles in the pre-generated file!")
else:
	print("[" + __file__ + "]" + "[INFO]" + " The largest three rectangles areas are: " + str(areas))