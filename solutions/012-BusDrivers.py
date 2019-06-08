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
## Task: 012-BusDrivers
## We have information about a bus schedule and the measured bus travel times. Based on these informations
## we want to create a mini statistics about the bus drivers and travel times.
##
## The selected route is Eger to Salgotarjan.
##
## We have a text file, which contains the bus drivers identification number and the travel times.
## The file fist column is the identification number the second is the travel times in minutes.
## Also we have another text file, which contains the bus drivers identification numbers and the divers name.
## The file first column is the identification number the second is the drivers firstname.
##
## The tasks are the following:
##	- Calculates every bus driver average travel times and print it with the bus drivers names.
##	- Sort the average travel times and print the fastest and the slowest bus driver names and average times.
##	- What was the best single travel time and who did it?
##
## Extra task-1:
##	- Get the average travel times from all travel times. The route is ~64 km long. Calculate the average bus speed in km/h.
##
## Extra task-2:
##	We want to create two groups of bus drivers for return type routes, so one driver leading the bus to Salgotarjan from Eger
##	and an another driver to Eger from Salgotarjan. The driver choose strategy is the following: the driver with the best average
##	travel time grouped with the driver with slowest average time, recursively. If the bus drivers count is an odd number, the
##	last unmatched bus driver will be grouped by himself.
##
##	For example:
##		The drivers sorted by the average travel times: a,b,c,d,e
##		The groups: (a,e), (b,d), (c,c)
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author