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
## @implementation-author