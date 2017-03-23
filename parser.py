#!/usr/bin/env python

import sys

"""
Usage: parser.py [file] [function] [target]
Takes an input file, a function to execute, and a target to parse for
"""
availableFunctions = 'wordCount, lemmaCount, tagCount, wordsWithTag, lemmasWithTag, unanalyzedLemmas, multiwords_words, multiwords_lemmas'

#http://wiki.apertium.org/wiki/List_of_symbols
global_tags = ['n', 'vblex', 'vbmod', 'vbser', 'vbhaver', 'vaux', 'adj', 'post', 'adv', 'preadv', 'postadv', 'mod', 'det', 'prn', 'pr', 'num', 'np', 'ij', 'cnjcoo', 'cnjsub', 'cnjadv', 'sent', 'cm', 'lquot', 'rquot', 'lpar', 'rpar', 'f', 'm', 'nt', 'ma', 'mi', 'mp', 'mn', 'fn', 'mf', 'mfn', 'ut', 'un', 'GD', 'sg', 'pl', 'sp', 'du', 'ct', 'coll', 'ND', 'cnt', 'unc', 'nom', 'acc', 'dat', 'gen', 'dg', 'voc', 'abl', 'ins', 'loc', 'prp', 'tra', 'ill', 'ine', 'ade', 'all', 'abe', 'ess', 'par', 'dis', 'com', 'soc', 'prl', 'actv', 'pass', 'pasv', 'midv', 'nactv', 'pres', 'pret', 'past', 'imp', 'inf', 'aor', 'pp', 'pp2', 'pp3', 'pprs', 'get', 'supn', 'pri', 'prii', 'fti', 'fts', 'cni', 'plu', 'pmp', 'prs', 'pis', 'ifi', 'aff', 'itg', 'neg', 'p1', 'p2', 'p3', 'impsers']

def main():
    #checks for correct command-line input
    if len(sys.argv) != 4:
        print "usage: python ./parser.py [file] [function] [target] \n \
            file: a file tagged according to apertium sttream format \n \
            function: %s \n \
            target: a tag, a word, or 0 depending on which function is being used" % availableFunctions
        exit(1)
    #import command-line arguments
    filename = str(sys.argv[1])
    function = str(sys.argv[2])
    target = str(sys.argv[3])
    #opens the input file
    file = open(filename)
    text = file.read()
    #strips whitespace from the text for all functions except for the multiwords ones
    if function != 'multiwords_words' and function != 'multiwords_lemmas':
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
    elif function == 'unanalyzedLemmas':
            print unanalyzedLemmas(lexicalUnits)
    elif function == 'multiwords_words':
            print multiwords_words(lexicalUnits)
    elif function == 'multiwords_lemmas':
            print multiwords_lemmas(lexicalUnits)
    else:
        print 'function not valid \navailable functions: %s' % availableFunctions
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
@prints 'unanalyzed' if it is unanalyzed
"""
def lemmaCount(lexicalUnits, target):
    lemmas = {} #maps words to the number of times it appears
    for lexicalUnit in lexicalUnits:
        lemma = stripForLemma(lexicalUnit)
        lemma = lemma.lower()
        lemmas[lemma] = lemmas.get(lemma,0) + 1
    if lemmas.get('*'+target,0) > 0:
        print 'unanalyzed'
        return lemmas.get('*'+target,0)
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
@returns a list of all unanalyzed lemmas in alphabetical order
"""
def unanalyzedLemmas(lexicalUnits):
    unanalyzedLemmas = {}
    for lexicalUnit in lexicalUnits:
        if '*' in lexicalUnit:
            lemma = stripForLemma(lexicalUnit)
            lemma = lemma.lower()
            unanalyzedLemmas[lemma] = unanalyzedLemmas.get(lemma,0) + 1
    return sorted(unanalyzedLemmas.keys())

"""
@returns a list of multiword words in alphabetical order
"""
def multiwords_words(lexicalUnits):
    multiwords = {}
    for lexicalUnit in lexicalUnits:
        if '#' in lexicalUnit:
            multiword = stripForWord(lexicalUnit)
            multiword = multiword.lower()
            multiwords[multiword] = multiwords.get(multiword,0) + 1
    return sorted(multiwords.keys())

"""
@returns a list of multiword lemmas in alphabetical order
"""
def multiwords_lemmas(lexicalUnits):
    multiwords = {}
    for lexicalUnit in lexicalUnits:
        if '#' in lexicalUnit:
            wordParsed = False
            hashFound = False
            multiword = ''
            lexicalUnit = lexicalUnit.partition('/')[2]
            for c in lexicalUnit:
                if c == '<':
                    wordParsed = True
                elif c == '#':
                    hashFound = True
                if not wordParsed: 
                    multiword += c
                elif hashFound and c != '#' and c != '$':
                    multiword += c
            multiword = multiword.strip()
            multiwords[multiword] = multiwords.get(multiword,0) + 1
    return sorted(multiwords.keys())         

"""
@returns the tags of the lexical unit stripped of word and lemma
"""
def stripForTags(lexicalUnit):
    lexicalUnit = lexicalUnit.partition('<')[1]+lexicalUnit.partition('<')[2]
    lexicalUnit = lexicalUnit.partition('#')[0]
    return lexicalUnit

"""
@returns the word of the lexical unit stripped of lemma and tags
"""
def stripForWord(lexicalUnit):
    lexicalUnit = lexicalUnit.partition('<')[0]
    lexicalUnit = lexicalUnit.partition('/')[0]
    return lexicalUnit

"""
@returns the lemma of the lexical unit stripped of word and tags
"""
def stripForLemma(lexicalUnit):
    lexicalUnit = lexicalUnit.partition('<')[0]
    lexicalUnit = lexicalUnit.partition('/')[2]
    lexicalUnit = lexicalUnit.partition('$')[0]
    return lexicalUnit

if __name__ == "__main__":
    main()
