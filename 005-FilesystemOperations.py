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
## Task: 005-FilesystemOperations:
## Creates a program which can handle filesystem operations.
##
## The required operations:
##	* List files from a specific folder.
##	* Copy one file from a path to another target path (the file name remains the same).
##	* Move one file from a specific folder to another target path (the file name can be changed).
##
## The program main input parameter is the usage mode (files listing (ls), copy file (cp), move file (mv)).
## After that the user can be type the other inputs into the program, based on the selected mode requirements.
##
## You have to check that the input parameters are correct, before the program tries to do a file operation.
## For example: the selected directory exists or not?
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author Kishazi "janohhank" Janos

# This module provides a portable way of using operating system dependent functionality.
import os
# The shutil module offers a number of high-level operations on files and collections of files.
import shutil
# Import argparse package for easier command line argument parsing.
import argparse

# Lists all files in a given directory.
def listFiles(inputDirPath):
	if os.path.isdir(inputDirPath) is False:
		raise Exception("The input path does not denote a directory: " + inputDirPath)

	print("[" + __file__ + "]" + "[INFO]" + " The " + inputDirPath + " contains these files:")
	for item in os.listdir(inputDirPath):
		if os.path.isfile(os.path.join(inputDirPath, item)):
			print(item)

# Copies file from an input path to the target path the file name is the same as the original file name.
def copyFile(inputFilePath, targetDirectory):
	if os.path.isfile(inputFilePath) is False:
		raise Exception("The input path does not denote a file: " + inputFilePath)

	if os.path.isdir(targetDirectory) is False:
		raise Exception("The target path does not denote a directory: " + targetDirectory)

	targetFileName = os.path.basename(inputFilePath)
	try:
		shutil.copyfile(inputFilePath, os.path.join(targetDirectory, targetFileName))
	except shutil.Error as error:
		print("[" + __file__ + "]" + "[ERROR]" + " Error caught in copyFile: " + error)
		sys.exit
	except IOError as ioError:
		print("[" + __file__ + "]" + "[ERROR]" + " Error caught in copyFile: " + ioError)
		sys.exit

# Moves file from an input path to the target path and ranames the file if necessary.
def moveFile(inputFilePath, targetFilePath):
	if os.path.isfile(inputFilePath) is False:
		raise Exception("The input path does not denote a file: " + inputFilePath)

	if os.path.isfile(targetFilePath) is True:
		raise Exception("In the target directory the file already exists: " + targetFilePath)

	try:
		shutil.move(inputFilePath, targetFilePath)
	except shutil.Error as error:
		print("[" + __file__ + "]" + "[ERROR]" + " Error caught in move: " + error)
		sys.exit
	except IOError as ioError:
		print("[" + __file__ + "]" + "[ERROR]" + " Error caught in move: " + error)
		sys.exit

parser = argparse.ArgumentParser(description="005-FilesystemOperations.")
parser.add_argument(
	"--mode",
	required=True,
	choices=["ls", "cp", "mv"],
	help="Program modes, it can be [ls,cp,mv]. Listing files from a directory, copy a file or move a file."
)

args = parser.parse_args()
mode = str(args.mode)

print("[" + __file__ + "]" + "[INFO]" + " Selected mode is: " + mode)

if(mode == "ls"):
	inputDirPath = str(input("[" + __file__ + "]" + "[INFO]" + " Please enter the path of the folder: "))
	listFiles(inputDirPath)
elif(mode == "cp"):
	inputFilePath = str(input("[" + __file__ + "]" + "[INFO]" + " Please enter the path of the file: "))
	targetDirectory = str(input("[" + __file__ + "]" + "[INFO]" + " Please enter the target directory path: "))
	copyFile(inputFilePath, targetDirectory)
elif(mode == "mv"):
	inputFilePath = str(input("[" + __file__ + "]" + "[INFO]" + " Please enter the path of the file: "))
	targetFilePath = str(input("[" + __file__ + "]" + "[INFO]" + " Please enter the target file path: "))
	moveFile(inputFilePath, targetFilePath)
else:
	raise Exception("Unhandled mode type: " + mode)