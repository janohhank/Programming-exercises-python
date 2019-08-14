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
## Task: 011-RunningCompetition
## We have information about a running competition, but a we got a little problem.
##
## The players identification numbers and laptimes are in a text file, and we can't create statistics about the players whole perfomance.
## This text file's first column is the ID number and a second is the laptime in second.
## What are these statistics:
##	- Every player total runtimes (sum of laptimes). Player ID - total runtime.
##	- Sorted list about the total runtimes. Best 10 players.
##	- What was the best single laptime and who did it?
##
## Also we have another file which contains the player identification numbers and the players name.
## We want to know the best 10 player names also, to we give them a medal.
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
'' Gives the laptimes associated to the player IDs in a dictionary.
'''
def getLaptimesForPlayers(inputFilePathLaptime):
	try:
		inputFileLaptime = open(inputFilePathLaptime, "r")
	except IOError as ioError:
		print("[" + __file__ + "]" + "[ERROR]" + ioError)
		sys.exit

	laptimesMap = {}
	for line in inputFileLaptime.readlines():
		lineElements = line.split(' ')

		playerID = int(lineElements[0])
		laptime = int(lineElements[1])

		laptimes = laptimesMap.get(playerID, [])
		laptimes.append(laptime)
		laptimesMap[playerID] = laptimes

	inputFileLaptime.close()

	return laptimesMap

'''
'' Gives the player names associated to the player IDs in a dictionary.
'''
def getPlayerNamesForIDs(inputFilePathNameID):
	try:
		inputFileNameID = open(inputFilePathNameID, "r")
	except IOError as ioError:
		print("[" + __file__ + "]" + "[ERROR]" + ioError)
		sys.exit

	playerNamesMap = {}
	for line in inputFileNameID.readlines():
		lineElements = line.split(' ')

		playerID = int(lineElements[0])
		playerName = str(lineElements[1]).rstrip()

		playerNamesMap[playerID] = playerName

	inputFileNameID.close()

	return playerNamesMap

'''
'' Gives the player race times associated to the player IDs in a dictionary.
'''
def getPlayersRaceTime(laptimesMap):
	playerRaceTimesMap = {}
	for playerID, laptimes in laptimesMap.items():
		sumLaptime = int(0)
		for laptime in laptimes:
			sumLaptime += laptime
		playerRaceTimesMap[playerID] = sumLaptime
	return playerRaceTimesMap

'''
'' Gives best lap time(s) (if the results has equal times) in a dictionary.
'' Player ID associated to the best laptime.
'''
def getBestLaptime(laptimesMap):
	bestLaptimes = {}
	minLaptime = float('inf')
	for playerID, laptimes in laptimesMap.items():
		laptimes.sort()
		currentMin = laptimes[0]
		if(currentMin < minLaptime):
			minLaptime = currentMin
			bestLaptimes.clear()
			bestLaptimes[playerID] = minLaptime
		elif(currentMin == minLaptime):
			bestLaptimes[playerID] = minLaptime
	return bestLaptimes

parser = argparse.ArgumentParser(description="011-RunningCompetition.")
parser.add_argument("--inputFilePathNameID",required=True,type=str,help="Pre-generated input file path which contains the ID-NAME associations.")
parser.add_argument("--inputFilePathLaptime",required=True,type=str,help="Pre-generated input file path which contains the ID-LAPTIME associations.")

args = parser.parse_args()
inputFilePathNameID = args.inputFilePathNameID
inputFilePathLaptime = args.inputFilePathLaptime

if(os.path.isfile(inputFilePathNameID) is False):
	raise Exception("The input path does not denote a file: " + inputFilePathNameID)
if(os.path.isfile(inputFilePathLaptime) is False):
	raise Exception("The input path does not denote a file: " + inputFilePathLaptime)

# Get laptimes associated to player IDs (a dictionary, key=playerID, value=laptimes list)
laptimesMap = getLaptimesForPlayers(inputFilePathLaptime)

# Get player names associated to player IDs (a dictionary, key=playerID, value=playerName)
playerNamesMap = getPlayerNamesForIDs(inputFilePathNameID)

# Get player race time associated to player IDs (a dictionary, key=playerID, value=racetime)
playerRaceTimesMap = getPlayersRaceTime(laptimesMap)

# Get best lap times associated to player IDs (a dictionary, key=playerID, value=laptime)
bestLaptimes = getBestLaptime(laptimesMap)

# Generate a sorted lists of race times with IDs.
sortedRaceTimes = sorted(playerRaceTimesMap.items(), key=operator.itemgetter(1))

print("[" + __file__ + "]" + "[INFO]" + " List of players race times: ")
for playerID, raceTime in playerRaceTimesMap.items():
	print("[" + __file__ + "]" + "[INFO]\t" + playerNamesMap[playerID] + " time is:\t" + str(raceTime))

print()
print("[" + __file__ + "]" + "[INFO]" + " List of best 10 players: ")
counter = int(0)
index = int(0)
previousRaceTime = int(-1)
cycleThreshold = min(10,len(sortedRaceTimes))
while(counter < cycleThreshold):
	playerID = sortedRaceTimes[index][0]
	playerRaceTime = sortedRaceTimes[index][1]

	if(playerRaceTime != previousRaceTime):
		counter += 1

	print("[" + __file__ + "]" + "[INFO]\t" + playerNamesMap[playerID] + " is the\t" + str(counter) + ".")

	previousRaceTime = playerRaceTime
	index += 1

print()
print("[" + __file__ + "]" + "[INFO]" + " Best laptime: ")
for playerID, laptime in bestLaptimes.items():
	print("[" + __file__ + "]" + "[INFO]\t" + playerNamesMap[playerID] + " with time:\t" + str(laptime))