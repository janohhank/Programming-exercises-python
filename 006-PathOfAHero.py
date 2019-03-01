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
## Task: 006-PathOfAHero:
## Create a program which can read the standard input and requires directions (ten pices in total).
##
## These directions (arrows in the keyboard) are defines a player movement in a game.
##
## The task is to help the player to reach the start point again. So you need to generate the reverse path.
##
## For exmaple a part of the program output:
## Player movement: up,up,left,right,up,left
## Reverse movement: right,down,left,right,down,down
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author Kishazi "janohhank" Janos

import curses

print(
	"[" + __file__ + "]"
	+ "[INFO]"
	+ " Welcome hero, you need to add your path (10 movement) to generate the reverse path."
)

# Initialize curses for the whole screen.
window = curses.initscr()
# Doesn't display the input character.
curses.noecho()
# Doesn't wait the enter, whit this curses reacts instantly.
curses.cbreak()
# Correct special keys handling from terminal (arrows).
window.keypad(True)
# Get current window dimension.
windowDimensions = window.getmaxyx()

step = 0
movements = []
while(step < 10):
	key = window.getch()
	if(key == curses.KEY_DOWN):
		window.clear()
		window.addstr(windowDimensions[0] / 2, windowDimensions[1] / 2, "KEY_DOWN")
		movements.append("DOWN")
	elif(key == curses.KEY_UP):
		window.clear()
		window.addstr(windowDimensions[0] / 2, windowDimensions[1] / 2, "KEY_UP")
		movements.append("UP")
	elif(key == curses.KEY_LEFT):
		window.clear()
		window.addstr(windowDimensions[0] / 2, windowDimensions[1] / 2, "KEY_LEFT")
		movements.append("LEFT")
	elif(key == curses.KEY_RIGHT):
		window.clear()
		window.addstr(windowDimensions[0] / 2, windowDimensions[1] / 2, "KEY_RIGHT")
		movements.append("RIGHT")
	else:
		window.clear()
		window.addstr(windowDimensions[0] / 2, windowDimensions[1] / 2, "Invalid key, you should use arrows.")
		continue
	step += 1

# Echoing again.
curses.echo()
# Cbreak off.
curses.nocbreak()
# Keypad decnfig.
window.keypad(False)
# Restore terminal to original operating mode.
curses.endwin()

reversePath = []
for movement in reversed(movements):
	if(movement == "DOWN"):
		reversePath.append("UP")
	elif(movement == "UP"):
		reversePath.append("DOWN")
	elif(movement == "LEFT"):
		reversePath.append("RIGHT")
	elif(movement == "RIGHT"):
		reversePath.append("LEFT")
	else:
		raise Exception("Unhandled movement direction: " + movement)

print("[" + __file__ + "]" + "[INFO]" + " The hero traverse this path: " + str(movements))
print("[" + __file__ + "]" + "[INFO]" + " The reverse path to home: " + str(reversePath))