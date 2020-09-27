'''
Program Name: NLTK Parser and Imager
Script Name: main.py
Version: 0.1
Python Version: 3.6
Author: Darian Lopez
Date: 2 June 19

Purpose:
The purpose of this program is to use the Natural Language Toolkit to analyze a set of text.
The NLTK provides sanitized and specifcally grouped text segments. These Text segments allow for the program to search accross raw data for phrases as key words.
 The Program can parse files and physical disks in binary formart block by block in search for the data.
  When the data is found the program outputs the block number index and what key word was found in a text file.
  It is essentially a raw preview and parse program of logical and physical data This becomes exponentially more useful
  when using words found images against hundreds of Gigabytes of data or even a couple Terabytes of data.
  The program was tested on one large text sample broken in to several text files.
'''

import hashlib
from datetime import datetime

import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import FreqDist as fdist
from nltk.corpus import stopwords
from gooey import Gooey
from gooey import GooeyParser
import os
import time

@Gooey(optional_cols=1, program_name="Python NLTK Parser and Imager")
def main():
    desc = "Create Mahcine Learning based search phrases. Then search accross raw data for them!"
    parser = GooeyParser(description=desc, add_help=False)
    parser.add_argument('--verbose', help='be verbose', dest='verbose',
                        action='store_true', default=True)

    subs = parser.add_subparsers(help='commands',prog='NLTK Builder',dest='command')

    parser_one = subs.add_parser('nltkParser', prog="NLTK Builder and Parser",help='Create Machine Learning Based Key Word Search Data with NLTK')
    parser_one.add_argument("--Text-File-Source", default="", widget='FileChooser', help='Select The Text (txt) Document for the program to analyze')
    parser_one.add_argument("--Data-To-Search", default="", widget='FileChooser',help='Select the Data Source you want to search the generated data against')
    parser_one.add_argument('--RawDiskName', default="", widget="TextField",help='Optional - Enter Your Raw Disk Drive Number you want to use ie 1,2,3,4....')

    parser_two = subs.add_parser('binaryDuplicator', prog="Binary Duplication", help='If you find the reslts you are looking for on your target data. Use This tool to create a byte for byte copy of it')
    parser_two.add_argument('--Source-File',default='',widget='FileChooser',help='Select the File/Data to copy')
    parser_two.add_argument('--Destination-Folder',default='',widget='DirChooser',help='Select where to save the copied data')
    parser_two.add_argument('--RawDiskName', default="", widget="TextField", help='Optional - Enter Your Raw Disk Drive Number you want to use ie 1,2,3,4....')

    args = parser.parse_args()

    if args.command == 'nltkParser':
        sFile =""
        dSearch =""

        if args.Text_File_Source !="" and checkDisk(args.RawDiskName):

            print("Checking Physical Drive")
            sFile = args.Text_File_Source
            dSearch = r'\\.\PhysicalDrive'+args.RawDiskName

            print(sFile)
            print(dSearch)

            values=""
            try:
                values = initSearchValuesfromTextFile(sFile)
            except:
                print("unable to generate values from file")
                return

            print("Checking for phrases {}".format(values))

            searchRawData(values, dSearch)


        else:
            if args.Text_File_Source !="" and args.Data_To_Search!= "":

                print("Not Checking Physical Drive")

                sFile =args.Text_File_Source
                dSearch = args.Data_To_Search

                print(sFile)
                print(dSearch)

                values = ""
                try:
                    values = initSearchValuesfromTextFile(sFile)
                except:
                    print("unable to generate values from file")
                    return

                print("Checking for phrases {}".format(values))

                searchRawData(values,dSearch)



    elif args.command == 'binaryDuplicator':

        sFile =""
        dFolder =os.getcwd()


        if args.RawDiskName !="" and checkDisk(args.RawDiskName):
            sFile = args.RawDiskName
        else:
            if args.Source_File !="":
                sFile =args.Source_File

        if args.Destination_Folder !="":
            dFolder = args.Destination_Folder

        else:
            print("Unable to parse Arguments")
            return

        imageIt(sFile, dFolder)

def checkDisk(name):
    try:
        with open(r'\\.\PhysicalDrive{}'.format(name), 'rb') as f:

            print("Found "+f.name)
        f.close()
        return True
    except Exception as e:
        print(e)
        return False

def initSearchValuesfromTextFile(file):

    with open(file, encoding='utf-8', errors="ignore")as f:
        text = f.read()
        stop_words = set(stopwords.words("english"))
        newTokenWords = sent_tokenize(" ".join([word for word in sent_tokenize(text) if word not in stop_words]))
        # print(text)
        print('\n')
        print('\n')
        # print(newTokenWords)
    f.close()

    return newTokenWords


def searchRawData(termList,data):

    print("raw data search")
    blocksFound =[]

    for w in termList:
        print("Looking for {} in {}".format(w,data))

        done = False
        placeHolder = 0
        with open(data, 'rb') as f:
            while not done:
                try:
                    block = f.read(1024)
                except Exception as e:
                    print(e)
                    break
                finally:
                    if block:
                        placeHolder = placeHolder + 1024
                        try:
                            print(block.decode("utf-8"))
                            if str(w) in block.decode('utf-8'):
                                if placeHolder not in blocksFound:
                                    blocksFound.append(placeHolder)
                                    report("{} found".format(w),placeHolder)
                        except:
                            pass
                    else:
                        done = True
        f.close()



def report(text,blockNum):

    with open("report.txt",'a+') as f:
        f.write(str(blockNum) +" | "+text+'\n')
    f.close()

def hashItOut(file):
    hashObj = hashlib.md5()

    done= False
    with open(file, 'rb') as file:

        while not done:
            block = file.read(1024)
            if block:
                hashObj.update(block)
            else:
                hashValue = hashObj.hexdigest().upper()
                done = True
    return hashValue

def imageIt(source,dest):

    hashValueFinal = hashItOut(source)
    outputFile = str(int(time.time()))
    with open(source, "rb") as f1:

        with open(outputFile, "wb") as f2:
            size1 = f1.__sizeof__()
            size2 = f2.__sizeof__()
            print("size of origina file: " + str(size1))
            while True:

                b = f1.read(1024)
                size1 -= 1024
                if(size1<0):
                    size1=0
                print("bytes left to copy: "+str(size1))
                if b:
                    f2.write(b)
                else:
                    break

    f1.close()
    f2.close()
    secondHash = hashItOut(outputFile)
    os.rename(outputFile, dest +"/"+ outputFile)

    print("First file >> ",source, " MD5 >> ",hashValueFinal)
    print("Second file >> ",outputFile," MD5 >> ",secondHash)



if __name__ == '__main__':
   main()