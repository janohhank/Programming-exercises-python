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
## Task: 010-Functions:
## This excersive focus on basic function implementations.
## In this exercise you need to implement all task to a function def and test this functions
## at the end of the script.
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author Kishazi "janohhank" Janos

# This module provides a portable way of using operating system dependent functionality.
import os
# Import math package for mathematical functions.
import math

# 1. task
# Create a function which has one parameter: a text file path.
# This function prints the file content into the standard output.
def readTextFile(filePath):
	if(os.path.isfile(filePath) is False):
		raise Exception("The input path does not denote a directory: " + filePath)
	try:
		textFile = open(filePath,"r")
	except IOError as ioe:
		print("[" + __file__ + "]" + "[ERROR]" + "I/O error " + ioe.errno + " " + ioe.strerror)
		sys.exit
	except:
		print("[" + __file__ + "]" + "[ERROR]" + "Unexpected error " + sys.exc_info()[0])
		sys.exit

	print(textFile.read())

# 2. task
# Create a function which has one parameter: a text file path.
# This function counts the words and sentences in the text file
# and returns these values.
def countWordsAndSenteces(filePath):
	if(os.path.isfile(filePath) is False):
		raise Exception("The input path does not denote a directory: " + filePath)
	try:
		textFile = open(filePath,"r")
	except IOError as ioe:
		print("[" + __file__ + "]" + "[ERROR]" + "I/O error " + ioe.errno + " " + ioe.strerror)
		sys.exit
	except:
		print("[" + __file__ + "]" + "[ERROR]" + "Unexpected error " + sys.exc_info()[0])
		sys.exit

	words = 0
	sentences = 0
	for character in textFile.read():
		if(character == ' '):
			words += 1
		elif(character == '.' or character == '?' or character == '!'):
			sentences += 1
	return words,sentences

# 3. task
# Create a function which has parameters: 2D vector coordinates.
# This function calculates and returns the magnitude (length) of the vector.
def vectorMagnitude(coordinateX, coordinateY):
	return math.sqrt(math.pow(coordinateX,2) + math.pow(coordinateY,2))

# 4. task
# Create a function which has two parameters: two Python list with numbers.
# The function join together the lists, the first list element next to the second list element etc...
# After that returns the result list.
# listA(a,b,c), listB(1,2,3,4) -> resultList(a,1,b,2,c,3,4)
def mergingLists(listA, listB):
	if(len(listA) == 0):
		return listB
	elif(len(listB) == 0):
		return listA

	minListSize = min(len(listA), len(listB))

	resultList = []
	for i in range(0, minListSize):
		resultList.append(listA[i])
		resultList.append(listB[i])
	listA = listA[minListSize:]
	listB = listB[minListSize:]

	if(len(listA) > 0):
		resultList.extend(listA)
	if(len(listB) > 0):
		resultList.extend(listB)
	return resultList

# 0. task
# After this comment write the tests of the defined functions.
# Call the function with correct and wrong parameters also.
# Handle the possible errors.
textFilePath = "/home/janohhank/GitWorking/ProgrammingExercisesPython/resources/010-Functions-Text-File.txt"

print("[" + __file__ + "]" + "[INFO]" + " Task 1, the file text:")
readTextFile(textFilePath)

words, sentences = countWordsAndSenteces(textFilePath)
print(
	"[" + __file__ + "]"
	+ "[INFO]"
	+ " Task 2, the text file contains " + str(words) + " words and " + str(sentences) + " sentences."
)

magnitude = vectorMagnitude(5,10)
print(
	"[" + __file__ + "]"
	+ "[INFO]"
	+ " Task 3, the (5,10) vector magnitude is " + str(magnitude)
)

listA = ["a", "b", "c"]
listB = [1, 2, 3, 4]
mergedList = mergingLists(listA, listB)
print(
	"[" + __file__ + "]"
	+ "[INFO]"
	+ " Task 4, the merged list: " + str(mergedList)
)