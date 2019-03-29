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
## Task: 007-DataStructures:
## The main focus of this task is to get more knowladge of the data structures of Python
## and also get the a general programming knowladge about this topic.
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author Kishazi "janohhank" Janos

## A. List
## Python data structures documentation: https://docs.python.org/2/tutorial/datastructures.html#more-on-lists
## Based on the tutorials above:
## A/1. Create a list filled with random data.
print("[" + __file__ + "]" + "[INFO]" + "-----------------------------A/1 Create lists with random elements.")
numberElementList = [1,5,9,13,7,9]
mixedElementList = [1,5,'b',13,'a',9,'c']

## A/2. Print the list elements.
print("[" + __file__ + "]" + "[INFO]" + "-----------------------------A/2 Print list elements.")

print("\tPrint list (1) elements:")
print("\t" + str(numberElementList))
print("\tPrint list (2) elements:")
print("\t" + str(mixedElementList))

print("\tPrint list (1) elements with a loop:")
for element in numberElementList:
	print("\t" + str(element), end=' ')
print()

print("\tPrint list (2) elements with a loop:")
for element in mixedElementList:
	print("\t" + str(element), end=' ')
print()

## A/3. Print the list elements reverse.
print("[" + __file__ + "]" + "[INFO]" + "-----------------------------A/3 Print list elements reverse.")

print("\tPrint list (1) elements reveresed:")
for element in reversed(numberElementList):
	print("\t" + str(element), end=' ')
print()

## A/4. Add elements (min 2) and remove elements (min 2) from the list.
print("[" + __file__ + "]" + "[INFO]" + "-----------------------------A/4 Add and remove elements from the list.")
numberElementList.append(101)
numberElementList.append(110)

print("\tPrint enriched list (1) elements:")
print("\t" + str(numberElementList))

numberElementList.remove(1)
numberElementList.remove(9)
print("\tPrint reduced list (1) elements:")
print("\t" + str(numberElementList))

## A/5. Print the list size.
print("[" + __file__ + "]" + "[INFO]" + "-----------------------------A/5 Print list size.")

listSize = len(numberElementList)
print("\tModified list size: " + str(listSize))

## A/6. Print just the list elements which index is odd.
print("[" + __file__ + "]" + "[INFO]" + "-----------------------------A/6 Print specified list elements.")

listSize = len(numberElementList)
for i in range(listSize):
	if(i % 2 == 1):
		print("\t" + str(numberElementList[i]),end=' ')
print()

## B. Dictionary
## Python data structures documentation: https://docs.python.org/2/tutorial/datastructures.html#dictionaries
## Based on the tutorials above:
## B/1. Create a dictionary filled with random data.
print("[" + __file__ + "]" + "[INFO]" + "-----------------------------B/1 Create dictionary with random elements.")
dictionaryExample = {
  "apple": 14,
  "samsung": 28,
  "huawei": 5
}

## B/2. Print the dictionary elements (key, and value also).
print("[" + __file__ + "]" + "[INFO]" + "-----------------------------B/2 Print dictionary elements.")
print("\tPrint dictionary elements:")
print("\t" + str(dictionaryExample))

print("\tPrint dictionary elements with a loop:")
for element in dictionaryExample:
	print("\t" + str(element) + " " + str(dictionaryExample[element]),end=' ')
print()

## B/3. Add new element into the dictionary.
print("[" + __file__ + "]" + "[INFO]" + "-----------------------------B/3 Add new elements into dictionary.")
dictionaryExample["nokia"] = 2
dictionaryExample["apple"] = 10

print("\t" + str(dictionaryExample))

## B/4. Remove element from the dictionary.
print("[" + __file__ + "]" + "[INFO]" + "-----------------------------B/4 Remove elements from dictionary.")
dictionaryExample.pop("huawei")
try:
	dictionaryExample.pop("motorola")
except KeyError:
	print("\tCan't remove motorola because the dictionary doesn't contains such an element.")

print("\t" + str(dictionaryExample))

## B/5. Get a value which associated to a specific key.
print("[" + __file__ + "]" + "[INFO]" + "-----------------------------B/5 Get specified key-value.")
print("\tThe value for key samsung is: " + str(dictionaryExample["samsung"]));

## C. Algorithm on data structures
## C/1.	Create a list with random numbers, and implement an algorithm
##	which can sort the elements of the lists.
##	Don't use sort() method!
##	Don't use 3rd party code!
print("[" + __file__ + "]" + "[INFO]" + "-----------------------------C/1 Sorting algorithm.")
unsortedList = [5,1,3,9,13,4,5]
print("\tThe unsorted list: " + str(unsortedList))
unsortedListSize = len(unsortedList)
for i in range(unsortedListSize):
	for j in range(0, unsortedListSize - i - 1):
		if(unsortedList[j] > unsortedList[j+1]):
			unsortedList[j], unsortedList[j+1] = unsortedList[j+1], unsortedList[j]
print("\tThe sorted list: " + str(unsortedList))

## C/2.	You got input, in this case the 'carsColors' list.
##	We want to know the count of the cars according to their color.
##	In this task you must use dictionary to store the information and get the numbers.
##	Print the colors and the count of the cars which has this color.
carsColors = ['red','blue','red','white','white','red','blue','red','white','white','black','grey']
print("[" + __file__ + "]" + "[INFO]" + "-----------------------------C/2 Clustering algorithm.")

countedColors = {}
for color in carsColors:
	countedColors[color] = countedColors.get(color, 0) + 1

print("\tCounted colors dictionary: " + str(countedColors))