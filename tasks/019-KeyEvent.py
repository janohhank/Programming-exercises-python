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
## Task: 019-KeyEvent
##
## The below implemented code is a sample, how to use curses Python library.
## With this you can catch the keyboards events and write it into the monitor, not the terminal.
##
## In this task you learn how to works the event based systems. Yout need to catch the keyboard events
## and reacts them. Also you can write messages into the display (this time not the standard input),
## so basically this is an expert hello word task.
##
## After the line "curses.endwin()" you can use again the standard output with the terminal.
##
## IMPORTANT : Don't close the program with ctr + c, when the curses hold the monitor resource.
##
## 1. Read the curses documentation https://docs.python.org/3/howto/curses.html.
##    Understand the implement code sample.
##
## 2. Rewrite to the sample program to use the w-a-s-d keyboards not the arrows.
##    (you can display the keyboard code in the else branch)
##
## 3. Measure the ellapsed time between button presses, and write the ellapsed time into the monitor.
##
## 4. Store the measured ellapsed times and calculate the FPS of the keyboard pressing.
##    Print it into the standard output. Also you can increase the required keyboard number.
##
##
## Extra task: Write a blue, bold, and blinking hello word into the monitor.
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author

import curses

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

window.addstr("Welcome!")

requiredKeyboardCount = 10

step = 0
movements = []
while(step < requiredKeyboardCount):
key = window.getch()
if(key == curses.KEY_DOWN):
window.clear()
window.addstr(int(windowDimensions[0] / 2), int(windowDimensions[1] / 2), "KEY_DOWN")
movements.append("DOWN")
elif(key == curses.KEY_UP):
window.clear()
window.addstr(int(windowDimensions[0] / 2), int(windowDimensions[1] / 2), "KEY_UP")
movements.append("UP")
elif(key == curses.KEY_LEFT):
window.clear()
window.addstr(int(windowDimensions[0] / 2), int(windowDimensions[1] / 2), "KEY_LEFT")
movements.append("LEFT")
elif(key == curses.KEY_RIGHT):
window.clear()
window.addstr(int(windowDimensions[0] / 2), int(windowDimensions[1] / 2), "KEY_RIGHT")
movements.append("RIGHT")
else:
window.clear()
window.addstr(int(windowDimensions[0] / 2), int(windowDimensions[1] / 2), "Invalid key, you should use arrows.")
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