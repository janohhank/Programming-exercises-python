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
## @implementation-author Kishazi "janohhank" Janos

# This module provides a portable way of using operating system dependent functionality.
import os
# Import argparse package for easier command line argument parsing.
import argparse
# The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python.
import operator

'''
'' Gives the travel times associated to the bus driver IDs in a dictionary.
'''
def getTravelTimesForBusDrivers(inputFilePathTravelTimes):
	try:
		inputFileTravelTimes = open(inputFilePathTravelTimes, "r")
	except IOError as ioError:
		print("[" + __file__ + "]" + "[ERROR]" + ioError)
		sys.exit

	travelTimesMap = {}
	for line in inputFileTravelTimes.readlines():
		lineElements = line.split(' ')

		busDriverID = int(lineElements[0])
		travelTime = int(lineElements[1])

		travelTimes = travelTimesMap.get(busDriverID, [])
		travelTimes.append(travelTime)
		travelTimesMap[busDriverID] = travelTimes

	inputFileTravelTimes.close()

	return travelTimesMap

'''
'' Gives the bus driver names associated to the bus driver IDs in a dictionary.
'''
def getBusDriverNamesForIDs(inputFilePathNameID):
	try:
		inputFileNameID = open(inputFilePathNameID, "r")
	except IOError as ioError:
		print("[" + __file__ + "]" + "[ERROR]" + ioError)
		sys.exit

	busDriverNamesMap = {}
	for line in inputFileNameID.readlines():
		lineElements = line.split(' ')

		busDriverID = int(lineElements[0])
		busDriverName = str(lineElements[1]).rstrip()

		busDriverNamesMap[busDriverID] = busDriverName

	inputFileNameID.close()

	return busDriverNamesMap

'''
'' Gives the bus driver average travel times associated to the bus driver IDs in a dictionary.
'''
def getAverageTravelTimesMap(travelTimesMap):
	busDriverAverageTravelTimesMap = {}
	for busDriverID, travelTimes in travelTimesMap.items():
		sumtravelTime = int(0)
		for travelTime in travelTimes:
			sumtravelTime += travelTime
		busDriverAverageTravelTimesMap[busDriverID] = sumtravelTime / len(travelTimes)
	return busDriverAverageTravelTimesMap

'''
'' Gives best single travel time(s) (if the results has equal times) in a dictionary.
'' Bus driver ID associated to the best travel time.
'''
def getBestTravelTime(travelTimesMap):
	bestTravelTimes = {}
	minTravelTime = float('inf')
	for busDriverID, travelTimes in travelTimesMap.items():
		travelTimes.sort()
		currentMin = travelTimes[0]
		if(currentMin < minTravelTime):
			minTravelTime = currentMin
			bestTravelTimes.clear()
			bestTravelTimes[busDriverID] = minTravelTime
		elif(currentMin == minTravelTime):
			bestTravelTimes[busDriverID] = minTravelTime
	return bestTravelTimes

parser = argparse.ArgumentParser(description="012-BusDrivers.")
parser.add_argument("--inputFilePathNameID",required=True,type=str,help="Pre-generated input file path which contains the ID-NAME associations.")
parser.add_argument("--inputFilePathTravelTimes",required=True,type=str,help="Pre-generated input file path which contains the ID-TRAVEL_TIME associations.")

args = parser.parse_args()
inputFilePathNameID = args.inputFilePathNameID
inputFilePathTravelTimes = args.inputFilePathTravelTimes

if(os.path.isfile(inputFilePathNameID) is False):
	raise Exception("The input path does not denote a file: " + inputFilePathNameID)
if(os.path.isfile(inputFilePathTravelTimes) is False):
	raise Exception("The input path does not denote a file: " + inputFilePathTravelTimes)

# Get travel times associated to bus driver IDs (a dictionary, key=bus driver ID, value=travel times list)
travelTimesMap = getTravelTimesForBusDrivers(inputFilePathTravelTimes)

# Get bus driver names associated to bus driver IDs (a dictionary, key=bus driver ID, value=bus driver name)
busDriverNamesMap = getBusDriverNamesForIDs(inputFilePathNameID)

# Get average travel time map in a dictionary (a dictionary, key=bus driver ID, value=average travel time)
averageTravelTimesMap = getAverageTravelTimesMap(travelTimesMap)

# Get best average travel times associated to bus driver IDs (a dictionary, key=bus driver ID, value=travel time)
bestSindleTravelTimes = getBestTravelTime(travelTimesMap)

# Generate a sorted lists of travel times with IDs.
sortedAverageTravelTimesMap = sorted(averageTravelTimesMap.items(), key=operator.itemgetter(1))

print("[" + __file__ + "]" + "[INFO]" + " List of bus drivers average travel times: ")
for busDriverID, averageTravelTime in averageTravelTimesMap.items():
	print("[" + __file__ + "]" + "[INFO]\t" + busDriverNamesMap[busDriverID] + " time is:\t" + str(averageTravelTime))

print()
print("[" + __file__ + "]" + "[INFO]" + " Ordered list of fastest average travel times: ")
counter = int(0)
index = int(0)
previousTravelTime = int(-1)
while(counter < len(sortedAverageTravelTimesMap)):
	busDriverID = sortedAverageTravelTimesMap[index][0]
	busDriverTravelTime = sortedAverageTravelTimesMap[index][1]

	if(busDriverTravelTime != previousTravelTime):
		counter += 1

	print("[" + __file__ + "]" + "[INFO]\t" + busDriverNamesMap[busDriverID] + " is the\t" + str(counter) + ".")

	previousTravelTime = busDriverTravelTime
	index += 1

print()
print("[" + __file__ + "]" + "[INFO]" + " Best single travel time: ")
for busDriverID, travelTime in bestSindleTravelTimes.items():
	print("[" + __file__ + "]" + "[INFO]\t" + busDriverNamesMap[busDriverID] + " with time:\t" + str(travelTime))

print()
print("[" + __file__ + "]" + "[INFO]" + " Average bus speed (extra task-1): ")
travelTimesCount = 0
summedAllTravelTimes = 0
for busDriverID, travelTimes in travelTimesMap.items():
	travelTimesCount += len(travelTimes)
	summedAllTravelTimes += sum(travelTimes)
averageAllTravelTimes = float(summedAllTravelTimes) / float(travelTimesCount)
averageBusSpeed = 64.0 / (float(averageAllTravelTimes) / 60.0)
print("[" + __file__ + "]" + "[INFO]\t" + str(averageBusSpeed) + " km/h.")

print()
print("[" + __file__ + "]" + "[INFO]" + " Bus driver groups (extra task-2): ")
counter = int(0)
sortedAverageTravelTimesMapSize = len(sortedAverageTravelTimesMap)
while(counter < sortedAverageTravelTimesMapSize / 2):
	print(
		str(counter) + " group is: "
		+ busDriverNamesMap[sortedAverageTravelTimesMap[counter][0]]
		+ ","
		+ busDriverNamesMap[sortedAverageTravelTimesMap[sortedAverageTravelTimesMapSize - 1 - counter][0]]
	)
	counter += 1