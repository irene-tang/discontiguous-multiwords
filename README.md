# discontiguous-multiwords coding challenge
GSoC '17 coding challenge - Discontiguous Multiwords
(http://wiki.apertium.org/wiki/Ideas_for_Google_Summer_of_Code/Discontiguous_multiwords)

1. Install a language pair where one of the languages has discontiguous multiwords.
2. Write a stream processor for the output of `apertium-tagger -p -g` that parses character by character, respecting superblanks.
3. From a corpus, extract a test set of different sentences with discontiguous multiwords in it

**Stream Processor**
========================
**Usage**
--------------------
python ./parser.py [file] [function] [target]
Takes an input file, a function to execute, and a target to parse for
- file: text should be tagged according to `apertium-tagger -p -g`
- function: wordCount, lemmaCount, tagCount, wordsWithTag, lemmasWithTag
- target: a tag or a word

**examples:**
python ./parser file.txt wordCount dogs
python ./parser file.txt lemmaCount dog
python ./parser file.txt tagCount n
python ./parser file.txt wordsWithTag adj
python ./parser file.txt lemmasWithTag vbmod

**Available Functions**
--------------------
**wordCount:** prints how many times the word appears in the file
**lemmaCount:** prints how many times the lemma appears in the file
**tagCount:** prints how many words in the file contain the tag
**wordsWithTag**: prints a list of all the words that contain the tag, in alphabetical order
**lemmasWithTag**: prints a list of all the lemmas that contain the tag, in alphabetical order

**Characters**
--------------------
**Reserved:**
- '^ $' -- deliminates lexical units
- '/' -- delimites analyses in ambiguous lexical units
- '<>' -- encapsulates tags
- '{}' -- delimites chunks
- '\' -- escape character
**Special:**
- '\*' -- Unanalyzed word.
- '@' -- Untranslated lemma.
- '#' -- start of invariable part of multiword marker.
- '+' -- Joined lexical units
- '~' -- Word needs treating by post-generator.
- '[]' -- Superblanks
