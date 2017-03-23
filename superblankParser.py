#!/usr/bin/env python

import sys

"""
Usage: superblankParser.py [file]
Takes an input file, strips superblanks from the text and prints it on the screen
"""

def main():
    filename = str(sys.argv[1])
    file = open(filename)
    text = file.read()
    print strip(text)

def strip(text):
    strippedText = ''
    inSuperblank = False
    for c in text:
        if inSuperblank and c == ']':
            inSuperblank = False
        elif c == '[':
            inSuperblank = True
        else:
            strippedText += c            
    return strippedText

if __name__ == "__main__":
    main()
