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
## Task: 017-FileInfo
##
## The task is to get information about files from the disk.
## Your program need to be structured!
##
## 1. Create a filter method (def) which can filters the
## files based on it's extension.
## input: file path list, extensionFilterString
## output: file path list
## 2. Create a method which can iterate over the input directory
## recursively.
## input: directory path
## input: file path list
## 3. Create a method which can get file information (os.stat)
## from a file.
## input: file path
## output: file stat information dictionary
## 4. Create a method which can transform the file stat information
## and write the selected informations into an XML file.
## input: file stat information dictionary
## output: XML file path
##
## The program input parameter: folder directori(es), and file extension filter parameter.
## Use the methods which are defined above. Get the files from the directory,
## filter the files, get information about the filtered files and writes it into an XML.
##
## You need to design the result XML structure.
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author