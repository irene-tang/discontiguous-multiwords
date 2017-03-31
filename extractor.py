#!/usr/bin/env python

import sys
import re
from dictionary import global_multiwords

def main():
    #checks for correct command-line input
    if len(sys.argv) != 3:
        print "usage: python ./extractor.py [input file] [output file]"
        exit(1)
    #import command-line arguments
    inputFileName = str(sys.argv[1])
    outputFileName = str(sys.argv[2])
    #read the contents of the input file
    inputFile = open(inputFileName)
    text = inputFile.read()
    inputFile.close()
    #split the text string into a list of sentences, and strip leading/trailing whitespace
    sentences = re.split('[.!?]', text)
    sentences = [sentence.strip() for sentence in sentences]
    #extract a list of sentences that contain discontiguous multiwords
    foundSentences = findDiscontiguous(sentences)
    print foundSentences #################
    #write the sentences to the output file
    outputFile = open(outputFileName, 'w')
    for sentence in foundSentences:
        outputFile.write('%s\n' % sentence)
    outputFile.close()

def findDiscontiguous(sentences):
    foundSentences = []
    for sentence in sentences:
        words = sentence.split(" ")
        for i,word in enumerate(words):
            x = global_multiwords.get(word,None)
            if x != None:
                trailingWords = words[i+2:i+5]
                if any(i in x for i in trailingWords):
                    foundSentences.append(sentence)
    return foundSentences

if __name__ == "__main__":
    main()
