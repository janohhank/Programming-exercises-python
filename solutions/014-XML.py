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
## Task: 014-XML
## The task has a resource file "014-XML-Books.xml", which contains a books catalog.
## Use the following library: https://docs.python.org/2/library/xml.etree.elementtree.html
##
## 1. Read the XML and print the standard output of the authors name and books name.
## 2. Print the most expensive book name.
## 3. Print the books which are in "Science Fiction" genre.
##
## Extra task 1:
## Add a new book into the XML.
##
## Extra task 2:
## Change all the prices from pound to hungarian forint.
##
## @task-author Kishazi "janohhank" Janos
## @implementation-author Kishazi "janohhank" Janos

# This module provides a portable way of using operating system dependent functionality.
import os
# Import argparse package for easier command line argument parsing.
import argparse
# Implements a simple and efficient API for parsing and creating XML data.
import xml.etree.ElementTree

# Global varibale
gbpToHuf = float(358)

parser = argparse.ArgumentParser(description="014-XML.")
parser.add_argument("--inputXMLFilePath",required=True,type=str,help="The input XML file path.")
parser.add_argument("--modifiedXMLFilePath",required=True,type=str,help="The output XML file path.")

args = parser.parse_args()
inputXMLFilePath = args.inputXMLFilePath
modifiedXMLFilePath = args.modifiedXMLFilePath

if(os.path.isfile(inputXMLFilePath) is False):
	raise Exception("The input path does not denote a file: " + inputXMLFilePath)

tree = xml.etree.ElementTree.parse(inputXMLFilePath)
root = tree.getroot()

for book in root.findall("book"):
	authorName = book.find("author").text
	titleName = book.find("title").text
	print("[" + __file__ + "]" + "[INFO]" + " The author of the book is: " + authorName + ", and the book name is: " + titleName)

resultTitle = None
maximumPrice = float(0)
for book in root.findall("book"):
	titleName = book.find("title").text
	currentPrice = float(book.find("price").text)

	if(currentPrice > maximumPrice):
		maximumPrice = currentPrice
		resultTitle = titleName
print("[" + __file__ + "]" + "[INFO]" + " The most expensive book is: " + resultTitle + ", this book price is: " + str(maximumPrice))

scienceFictionBooks = []
for book in root.findall("book"):
	titleName = book.find("title").text
	genre = book.find("genre").text

	if(genre == "Science Fiction"):
		scienceFictionBooks.append(titleName)
print("[" + __file__ + "]" + "[INFO]" + " The science fiction books are: " + str(scienceFictionBooks))

# Inserting a new book.
newBook = xml.etree.ElementTree.Element("book")
author = xml.etree.ElementTree.SubElement(newBook,"author")
author.text = "Isaac Asimov"
title = xml.etree.ElementTree.SubElement(newBook,"title")
title.text = "Foundation"
genre = xml.etree.ElementTree.SubElement(newBook,"genre")
genre.text = "Science Fiction"
price = xml.etree.ElementTree.SubElement(newBook,"price")
price.text = "10"
root.insert(1,newBook)
print("[" + __file__ + "]" + "[INFO]" + " New book was inserted: Isaac Asimov - Foundation.")

# Modify books prices.
for book in root.findall("book"):
	currentPriceGBP = float(book.find("price").text)
	currentPriceHUF = currentPriceGBP * gbpToHuf
	book.find("price").text = str(currentPriceHUF)
tree.write(modifiedXMLFilePath)
print("[" + __file__ + "]" + "[INFO]" + " The GBP prices are modified and saved into the: " + str(modifiedXMLFilePath))