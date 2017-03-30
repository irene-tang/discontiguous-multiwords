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
    for i, c in enumerate(text):
        if i == 0:
            prev = ''
        else:
            prev = text[i-1]
        if inSuperblank and c == ']' and prev != '\\':
            inSuperblank = False
        elif c == '[' and prev != '\\':
            inSuperblank = True
        elif not inSuperblank:
            strippedText += c            
    return strippedText

if __name__ == "__main__":
    main()
