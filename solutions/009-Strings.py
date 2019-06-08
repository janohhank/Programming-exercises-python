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
## Task: 009-Strings:
## This exercise is based on the string operations in Python.
## Solve every task of the exercise and print the resut to the standard output.
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author Kishazi "janohhank" Janos

message="Hello, this is a Python program."

# 1. task
# Add a hashtag ('#') between every character of the message.
# The first character is a H and the last karacter is the '.'.
modifiedMessage_1=""
for character in message:
	if(character != ' ' and character != '.'):
		modifiedMessage_1+=character+'#'
	else:
		modifiedMessage_1+=character
print("[" + __file__ + "]" + "[INFO]" + " 1. task " + modifiedMessage_1)

# 2. task
# Change every 'L' character to '1', ecery 'e' to '3' and every a to '4'.
modifiedMessage_2=message
modifiedMessage_2=modifiedMessage_2.replace("l","1")
modifiedMessage_2=modifiedMessage_2.replace("e","3")
modifiedMessage_2=modifiedMessage_2.replace("a","4")
print("[" + __file__ + "]" + "[INFO]" + " 2. task " + modifiedMessage_2)

# 3. task
# Split the message into a list of string by the spaces.
splitMessage=message.split(' ')
print("[" + __file__ + "]" + "[INFO]" + " 3. task " + str(splitMessage))

# 4. task
# Change 'this' and 'Python' words to upper case in the message.
modifiedMessage_4=message
modifiedMessage_4=modifiedMessage_4.replace("this","THIS")
modifiedMessage_4=modifiedMessage_4.replace("Python","PYTHON")
print("[" + __file__ + "]" + "[INFO]" + " 4. task " + str(modifiedMessage_4))

# 5. task
# Save every words of the message into different files to the disk.
for word in splitMessage:
	tmpFile = open(word + ".txt",'w')
	tmpFile.write(word)
	tmpFile.close()
	print("[" + __file__ + "]" + "[INFO]" + " 5. task, saved file in: " + word + ".txt")

# 6. task
# Add your name after the 'Hello' in the message.
modifiedMessage_6=message
endPosition=modifiedMessage_6.find("Hello") + 5
modifiedMessage_6=modifiedMessage_6[ : endPosition] + " janohhank" + modifiedMessage_6[endPosition : ]
print("[" + __file__ + "]" + "[INFO]" + " 6. task " + str(modifiedMessage_6))

# 7. task
# Write the message reverse.
print("[" + __file__ + "]" + "[INFO] " + message[::-1])