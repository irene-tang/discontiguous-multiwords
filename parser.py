#!/usr/bin/env python

import sys

"""
Usage: parser.py [file] [function] [target]
Takes an input file, a function to execute, and a target to parse for
	file: text should be tagged according to apertium-tagger -g -p
	function: wordCount, lemmaCount, tagCount, wordsWithTag, lemmasWithTag
	target: a tag or a word
"""

#http://wiki.apertium.org/wiki/List_of_symbols
global_tags = ['n', 'vblex', 'vbmod', 'vbser', 'vbhaver', 'vaux', 'adj', 'post', 'adv', 'preadv', 'postadv', 'mod', 'det', 'prn', 'pr', 'num', 'np', 'ij', 'cnjcoo', 'cnjsub', 'cnjadv', 'sent', 'cm', 'lquot', 'rquot', 'lpar', 'rpar', 'f', 'm', 'nt', 'ma', 'mi', 'mp', 'mn', 'fn', 'mf', 'mfn', 'ut', 'un', 'GD', 'sg', 'pl', 'sp', 'du', 'ct', 'coll', 'ND', 'cnt', 'unc', 'nom', 'acc', 'dat', 'gen', 'dg', 'voc', 'abl', 'ins', 'loc', 'prp', 'tra', 'ill', 'ine', 'ade', 'all', 'abe', 'ess', 'par', 'dis', 'com', 'soc', 'prl', 'actv', 'pass', 'pasv', 'midv', 'nactv', 'pres', 'pret', 'past', 'imp', 'inf', 'aor', 'pp', 'pp2', 'pp3', 'pprs', 'get', 'supn', 'pri', 'prii', 'fti', 'fts', 'cni', 'plu', 'pmp', 'prs', 'pis', 'ifi', 'aff', 'itg', 'neg', 'p1', 'p2', 'p3', 'impsers']

def main():
    #checks for correct command-line input
    if len(sys.argv) != 4:
        print "usage: python ./parser.py [file] [function] [target] \n \
            file: a file tagged according to apertium sttream format \n \
            function: wordCount, lemmaCount, tagCount, wordsWithTag, lemmasWithTag \n \
            target: a tag or a word depending on the function"
        exit(1)
    #import command-line arguments
    filename = str(sys.argv[1])
    function = str(sys.argv[2])
    target = str(sys.argv[3])
    #opens the input file
    file = open(filename)
    text = file.read()
    #strips whitespace
    text = text.replace(' ','')
    #splits the text string into a list of lexical units
    lexicalUnits = text.split('^')
    lexicalUnits = lexicalUnits[1:]
    
    #executes the specified function
    if function == 'wordCount':
        print wordCount(lexicalUnits, target)
    elif function == 'lemmaCount':
    	print lemmaCount(lexicalUnits, target)
    elif function == 'tagCount':
        if validTag(target):
            print tagCount(lexicalUnits, target)
    elif function == 'wordsWithTag':
        if validTag(target):
            print wordsWithTag(lexicalUnits, target)
    elif function == 'lemmasWithTag':
        if validTag(target):
            print lemmasWithTag(lexicalUnits, target)
    else:
        print 'function not valid \n \
            available functions: wordCount, lemmaCount, tagCount, wordsWithTag, lemmasWithTag'
        exit(1)

"""
@throws error if the inputted target tag is valid
@returns true if not valid
"""
def validTag(tag):
    if tag not in global_tags:
        print 'tag not valid'
        exit(1)
    else:
        return True

"""
@returns a count of how many times the word is used
"""
def wordCount(lexicalUnits, target):
    words = {} #maps words to the number of times it appears
    for lexicalUnit in lexicalUnits:
        word = stripForWord(lexicalUnit)
        word = word.lower()
        words[word] = words.get(word,0) + 1
    return words.get(target,0)

"""
@returns a count of how many times the lemma is used
"""
def lemmaCount(lexicalUnits, target):
    lemmas = {} #maps words to the number of times it appears
    for lexicalUnit in lexicalUnits:
        lemma = stripForLemma(lexicalUnit)
        lemma = lemma.lower()
        lemmas[lemma] = lemmas.get(lemma,0) + 1
    return lemmas.get(target,0)

"""
@returns a count of how many words contain the tag
"""
def tagCount(lexicalUnits, target):
    tags = {} #maps tags to the number of times it appears
    for lexicalUnit in lexicalUnits:
        tag = ''
        lexicalUnit = stripForTags(lexicalUnit)
        for c in lexicalUnit:
            if c == '>':
            	tags[tag] = tags.get(tag,0) + 1
            	tag = ''
            elif c != '<':
                tag += c
    return tags.get(target,0)

"""
@returns a list all of the words that contain the tag in alphabetical order
"""
def wordsWithTag(lexicalUnits, target):
    words = {}
    for lexicalUnit in lexicalUnits:
    	if tagCount([lexicalUnit], target) > 0:
    		word = stripForWord(lexicalUnit)
    		word = word.lower()
    		words[word] = words.get(word,0) + 1
    return sorted(words.keys())


"""
@returns a list all of the lemmas that contain the tag in alphabetical order
"""
def lemmasWithTag(lexicalUnits, target):
    lemmas = {}
    for lexicalUnit in lexicalUnits:
    	if tagCount([lexicalUnit], target) > 0:
    		lemma = stripForLemma(lexicalUnit)
    		lemma = lemma.lower()
    		lemmas[lemma] = lemmas.get(lemma,0) + 1
    return sorted(lemmas.keys())

"""
@returns the tags of the lexical unit stripped of word and lemma
"""
def stripForTags(lexicalUnit):
    return lexicalUnit.partition('<')[1]+lexicalUnit.partition('<')[2]

"""
@returns the word of the lexical unit stripped of lemma and tags
"""
def stripForWord(lexicalUnit):
    lexicalUnit = lexicalUnit.partition('<')[0]
    return lexicalUnit.partition('/')[0]

"""
returns the lemma of the lexical unit stripped of word and tags
"""
def stripForLemma(lexicalUnit):
	lexicalUnit = lexicalUnit.partition('<')[0]
	return lexicalUnit.partition('/')[2]

if __name__ == "__main__":
    main()
