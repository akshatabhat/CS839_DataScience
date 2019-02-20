import sys,os
import argparse

def main(args):

    fd = open(args.fileName, "r")
    fileLines = fd.readlines()
    fd.close()

    filesDict = dict()
    fileText = ''
    fullTextFlag = 0
    fileName = ''

    for lines in fileLines:
        if 'Title:' in lines:
            splitLine = lines.split('Title: ')
            splitLine = splitLine[1]
            splitLine = splitLine.split('\n')
            fileName = splitLine[0]
            fileName = fileName.replace(" ","")
            filesDict[fileName] = fileText
            fileText = ''
        
        if lines == '\n':
            fullTextFlag = 0

        if 'Credit:' in lines:
            fullTextFlag = 0
        elif 'CREDIT:' in lines:
            fullTextFlag = 0
        elif 'Subject:' in lines:
            fullTextFlag = 0


        if fullTextFlag == 1:
            fileText += lines
            #print(fileText)

        if 'Full text:' in lines:
            fullTextFlag = 1
            splitLine = lines.split('Full text:')
            fileText += splitLine[1]

    count = 0
    for keys in filesDict:
        count += 1
        fd = open("%d.txt" %count , "w")
        fd.writelines(filesDict[keys])
        fd.close()
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-f','--file', type=str, required=True, dest='fileName', help='Filename')
    args = parser.parse_args();
    main(args)
