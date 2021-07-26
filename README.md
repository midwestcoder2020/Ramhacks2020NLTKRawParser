# Ramhacks2020NLTKRawParser (Updated 26 Jul 2021)
NLTKRawParser and Imager

(Best Digital Forensics Hack)

## Inspiration
When trying to locate data through logical or physical approaches, it can be difficult to decides which key words and phrases to use when parsing through data sets. Some tools provide similar ideas but require large amounts of time to prepare the do background tasks due to their overall robust nature. This introduces the need to parse a device in the logical or physical manner with less amount of extra computing or additional tasks/preprocessing involved. 

## What it does
The purpose of this program is to use the Natural Language Toolkit to analyze a set of text.
The NLTK provides sanitized and specifcally grouped text segments.
These Text segments allow for the program to search accross raw data for phrases as key words. 
The Program can parse files and physical disks in binary formart block by block in search for the data.
When the data is found the program outputs the block number index and what key word was found in a text file. 
It is essentially a raw preview and parse program of logical and physical data
This becomes exponentially more useful when using words found images against hundreds of Gigabytes of data or even  a couple Terabytes of data. The program was tested on one large text sample broken in to several text files. 


## How I built it
I used Python as my base programming language. I then utilized the Gooey library which is a UI wrapper for Python's ArgParse library and provides visual verbose functionality.

I then broke down the sub requirements into:

installation of NLTK and corresponding libraries

generate and obtain test data

build algorithm/functionality of Natural Language Processing NLTK to read from a text file and parse accordingly

Build algorithm and functionality to check and read physical disks and logical files in binary format.

Create robust and simple UI to allow the user to complete their task

Combine NLTK generated data set and binary parsing of data to sequentially iterate block by block through data

Create a simple logging/reporting functionality for use to look back into when task was complete so user can make on the fly triaging decisions.


## Challenges I ran into
Physical access to disks and binary parsing of files and physical disks

IO issues with opening closing writing to and from files

Parsing arguments given by user and handling exceptions

## Accomplishments that I'm proud of
Accessing and Parsing Raw Physical disks in Python with minimal overhead

Using NLP and NLTK to generate clean keys words and phrases

## What I learned
Using Natural Language Processing NLTK to read and tokenize and sanitize text( stop words)

combining IO of Raw physical disks

reading binary block by block

decoding binary to readable text.

improving error handling from binary IO

## What's next for NLTKParser

Improved performance through multithreading

Improved NLP and NLTK implementation

More Robust Reporting features
