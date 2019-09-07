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
## Task: 015-Traffic
## There are three resource file for this task:
## * 016-Traffic-4-6.txt
## * 016-Traffic-914A.txt
## * 016-Traffic-M3.txt
##
## These are the stops list of the public vehicles (4-6 tram, M3 subway and 914A bus).
## The first row of the file is the type of the public vehicles, the other rows are the
## stops (in ordered).
##
## 1. Reads the files and writes the stops every vehicles.
##
## 2. The user can add a stop name and the program gives the vehicles which stops at the current
## location. For example: "Corvin-negyed", every vehicles stops at this location.
##
## 3. The user can add two stops name and one vehicle, and the program writes how many stops
## are between the two location.
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author Kishazi "janohhank" Janos

# This module provides a portable way of using operating system dependent functionality.
import os
# Import argparse package for easier command line argument parsing.
import argparse

parser = argparse.ArgumentParser(description="016-Traffic.")
parser.add_argument("--tramFilePath",required=True,type=str,help="The file path of the tram stops.")
parser.add_argument("--busFilePath",required=True,type=str,help="The file path of the bus stops.")
parser.add_argument("--metroFilePath",required=True,type=str,help="The file path of the metro stops.")

args = parser.parse_args()
tramFilePath = args.tramFilePath
busFilePath = args.busFilePath
metroFilePath = args.metroFilePath

if(os.path.isfile(tramFilePath) is False):
	raise Exception("The input path does not denote a file: " + tramFilePath)
if(os.path.isfile(busFilePath) is False):
	raise Exception("The input path does not denote a file: " + busFilePath)
if(os.path.isfile(metroFilePath) is False):
	raise Exception("The input path does not denote a file: " + metroFilePath)

print("[" + __file__ + "]" + "[INFO]" + " Loading vehicle stops files.")

tramFile = open(tramFilePath)
busFile = open(busFilePath)
metroFile = open(metroFilePath)

vehiclesMap = {}

vehiclesMap["4-6"] = []
for line in tramFile.readlines():
	vehiclesMap["4-6"].append(line.rstrip())
vehiclesMap["914A"] = []
for line in busFile.readlines():
	vehiclesMap["914A"].append(line.rstrip())
vehiclesMap["M3"] = []
for line in metroFile.readlines():
	vehiclesMap["M3"].append(line.rstrip())

print("[" + __file__ + "]" + "[INFO]" + " Loaded vehicles and stops:\n " + str(vehiclesMap))

stopName = str(input("Please enter the selected stop name: "))

selectedVehicles = []
for vehicle, stops in vehiclesMap.items():
	for stop in stops:
		if(stop == stopName):
			selectedVehicles.append(vehicle)
			break

if(len(selectedVehicles) > 0):
	print("[" + __file__ + "]" + "[INFO]" + " At the selected stop: " + stopName + ", has station these vehicles: " + str(selectedVehicles))
else:
	print("[" + __file__ + "]" + "[INFO]" + " At the selected stop: " + stopName + ", there are no station for any vehicles in the files.")

vehicle = str(input("Please enter the selected vehicle name: "))
firstStop = str(input("Please enter the first stop name: "))
secondStop = str(input("Please enter the second stop name: "))

stopsList = vehiclesMap.get(vehicle,None)
if(stopsList is None):
	print("[" + __file__ + "]" + "[INFO]" + " There are no information about this vehicle in the files: " + vehicle)
else:
	if(firstStop == secondStop):
		print("[" + __file__ + "]" + "[INFO]" + " The selected two stops are the same!")

	if(firstStop in stopsList and secondStop in stopsList):
		stopCountBetweenStations = abs(stopsList.index(firstStop) - stopsList.index(secondStop))
		print("[" + __file__ + "]" + "[INFO]" + " There are " + str(stopCountBetweenStations) + " stations between the two stops!")
	else:
		print("[" + __file__ + "]" + "[INFO]" + " Not all stops are in the station list of the selected vehicle!")