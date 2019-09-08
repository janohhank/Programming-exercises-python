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
## Task: 018-CarStatistic
##
## In this task you need to read and write spreadsheet files (in this time .ods files).
## The used resource file is: CarStatistic.ods
##
## You need to interpret the contents of the file. This is a simple table of a car usage.
## After that you need to read the file content in Python with "pyexcel-ods" library:
##	* https://pythonhosted.org/pyexcel-ods/
## Of course if you find another ods reader library in Python and you can use that.
##
## 1. Write the value of all distance traveled in kilometer into the standard output.
##
## 2. Write the value of all refueled gasoline in liter into the standard output.
##
## 3. Calculate the car average consumption (consumption per 100 kilometers).
##
## 4. Calculate the average price of 1 liter gasoline.
##
## 5. Which refueling was the most expensive in 1 liter / Ft.
##
## 6. Create a code which can add a new row into the ods.
##    Add new refuling statics into the spreadsheet.
##    Get a new command line argument, the path of the extended result spreadsheet file.
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author Kishazi "janohhank" Janos

# This module provides a portable way of using operating system dependent functionality.
import os
# Import argparse package for easier command line argument parsing.
import argparse
# A wrapper library to read, manipulate and write data in ods format.
import pyexcel

parser = argparse.ArgumentParser(description="017-CarStatistic.")
parser.add_argument("--carStatisticFilePath",required=True,type=str,help="The file path of the car .ODS file.")
parser.add_argument("--extendedCarStatisticFilePath",required=True,type=str,help="The file path of the extended car .ODS file.")

args = parser.parse_args()
carStatisticFilePath = args.carStatisticFilePath
extendedCarStatisticFilePath = args.extendedCarStatisticFilePath

if(os.path.isfile(carStatisticFilePath) is False):
	raise Exception("The input path does not denote a file: " + carStatisticFilePath)

print("[" + __file__ + "]" + "[INFO]" + " Loading ods file.")

carData = pyexcel.get_book(file_name=carStatisticFilePath)
sheet = carData["CarData"]

print("[" + __file__ + "]" + "[INFO]" + " Data loaded successfully:\n" + str(carData))

traveledDistances = sheet.column[3]
print("[" + __file__ + "]" + "[INFO]" + " Traveled distances: " + str(traveledDistances))

refuledGasolines = sheet.column[2]
print("[" + __file__ + "]" + "[INFO]" + " Refuled gasolines: " + str(refuledGasolines))

sumTraveledDistances = int(0)
for traveledDistance in traveledDistances:
	try:
		sumTraveledDistances += int(traveledDistance)
	except ValueError:
		continue
print("[" + __file__ + "]" + "[INFO]" + " Sum traveled distances: " + str(sumTraveledDistances) + " km.")

sumRefuledGasoline = int(0)
for refuledGasoline in refuledGasolines:
	try:
		sumRefuledGasoline += int(refuledGasoline)
	except ValueError:
		continue
print("[" + __file__ + "]" + "[INFO]" + " Sum refuled gasolines: " + str(sumRefuledGasoline) + " liter.")

averageConsumption = float(sumRefuledGasoline) / (float(sumTraveledDistances) / 100.0)
print("[" + __file__ + "]" + "[INFO]" + " Average consumption: " + str(averageConsumption) + " per 100 km.")

refuelPrices = sheet.column[4]
print("[" + __file__ + "]" + "[INFO]" + " Refuel prices: " + str(refuelPrices))

refuelPricesPerLiter = []
for index in range(len(refuledGasolines)):
	try:
		refuelPricesPerLiter.append(float(refuelPrices[index]) / float(refuledGasolines[index]))
	except ValueError:
		refuelPricesPerLiter.append("N/A")
		continue

availableValues = int(0)
averageRefuelPricePerLiter = int(0)
for refuelPricePerLiter in refuelPricesPerLiter:
	try:
		averageRefuelPricePerLiter += float(refuelPricePerLiter)
		availableValues += 1
	except ValueError:
		continue

averageRefuelPricePerLiter = float(averageRefuelPricePerLiter) / float(availableValues)
print("[" + __file__ + "]" + "[INFO]" + " Average refuel price of 1 liter: " + str(averageRefuelPricePerLiter))

maxRefuelPricePerLiter = averageRefuelPricePerLiter
for refuelPricePerLiter in refuelPricesPerLiter:
	try:
		if(float(refuelPricePerLiter) > float(maxRefuelPricePerLiter)):
			maxRefuelPricePerLiter = refuelPricePerLiter
	except ValueError:
		continue
print("[" + __file__ + "]" + "[INFO]" + " Index of max refuel price per liter: " + str(refuelPricesPerLiter.index(maxRefuelPricePerLiter) - 1) + ", the value is: " +  str(maxRefuelPricePerLiter))

print("[" + __file__ + "]" + "[INFO]" + " Adding a new row into the spreadsheet.")
sheet.extend_rows([26,228781,20.0,1000,415])

carData.save_as(extendedCarStatisticFilePath)
print("[" + __file__ + "]" + "[INFO]" + " Saved the extended spreadsheet file into: " + str(extendedCarStatisticFilePath))