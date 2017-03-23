# Discontiguous Multiwords - Coding Challenge
**GSoC '17 coding challenge - Discontiguous Multiwords - Irene Tang**
(http://wiki.apertium.org/wiki/Ideas_for_Google_Summer_of_Code/Discontiguous_multiwords)

1. Install a language pair where one of the languages has discontiguous multiwords.
2. Write a stream processor for the output of `apertium-tagger -p -g` that parses character by character, respecting superblanks.
3. From a corpus, extract a test set of different sentences with discontiguous multiwords in it


**In this repository:**

- **superblankParser.py**: a stream processor that parses character by character (challenge #2)
- **parser.py:** a stream processor that does more stuff than superblankParser (challenge #2.5)
- **sample_texts:** sample texts for ./superblankParser.py and ./parser.py

**superblankParser.py**
========================
`python ./superblankParser.py [file]` <br />
Takes an input file, prints the text in the file stripped of superblanks


**parser.py**
========================
**Usage**
--------------------
`python ./parser.py [file] [function] [target]` <br />
Takes an input file, a function to execute, and a target to parse for
- file: text should be tagged according to `apertium-tagger -p -g`
- function: wordCount, lemmaCount, tagCount, wordsWithTag, lemmasWithTag, unanalyzedLemmas, multiwords_words, multiwords_lemmas'
- target: a tag, a word, or 0 depending on the function

**examples:**

`python ./parser file.txt wordCount dogs` <br />
`python ./parser file.txt lemmaCount dog` <br />
`python ./parser file.txt tagCount n` <br />
`python ./parser file.txt wordsWithTag adj` <br />
`python ./parser file.txt lemmasWithTag vbmod` <br />
`python ./parser file.txt unanalyzedLemmas 0` <br />
`python ./parser file.txt multiwords_words 0` <br />
`python ./parser file.txt multiwords_lemmas 0` <br />

**Available Functions**
--------------------
- **wordCount:** prints how many times the word appears in the file
- **lemmaCount:** prints how many times the lemma appears in the file
- **tagCount:** prints how many words in the file contain the tag
- **wordsWithTag:** prints a list of all the words that contain the tag, in alphabetical order
- **lemmasWithTag:** prints a list of all the lemmas that contain the tag, in alphabetical order
- **unanalyzedLemmas:** prints a list of all unanalyzed lemmas, in alphabetical order
- **multiwords_words:** prints a list of all multiwords in their word form, in alphabetical order
- **multiwords_lemmas:** prints a list of all multiwords in their lemma form, in alphabetical order

**Characters**
--------------------
**Reserved:**
- '^ $' -- deliminates lexical units
- '/' -- delimites analyses in ambiguous lexical units
- '<>' -- encapsulates tags
- '{}' -- delimites chunks
- '\\' -- escape character
  
**Special:**
- '\*' -- Unanalyzed word.
- '@' -- Untranslated lemma.
- '#' -- start of invariable part of multiword marker.
- '+' -- Joined lexical units
- '~' -- Word needs treating by post-generator.
- '[]' -- Superblanks
