# Discontiguous Multiwords - Coding Challenge
**GSoC '17 coding challenge - Discontiguous Multiwords - Irene Tang**
(http://wiki.apertium.org/wiki/Ideas_for_Google_Summer_of_Code/Discontiguous_multiwords)

1. Install a language pair where one of the languages has discontiguous multiwords.
2. Write a stream processor for the output of `apertium-tagger -p -g` that parses character by character, respecting superblanks.
3. From a corpus, extract a test set of different sentences with discontiguous multiwords in it.


**In this repository:**

- **superblankParser.py**: a stream processor that parses character by character (challenge #2)
- **parser.py:** a stream processor that does more stuff than superblankParser (challenge #2.5)
- **extractor.py:** a script that extracts sentences with discontiguous multiwords (challenge #3)
- **extractor_output.txt:** a sample document containing sentences with discontinuous multiwords, created by running extractor.py and manually marked to distinguish between real discontinuous multiwords from non-real discontinuous multiwords (challenge #3)
- **sample_texts:** a folder containing some sample texts


**superblankParser.py** challenge #2
=========================================
`python ./superblankParser.py [file]` <br />
Takes an input file, prints the text in the file stripped of superblanks.


**parser.py** challenge #2.5
=========================================
**Usage**

`python ./parser.py [file] [function] [target]` <br />
Takes an input file, a function to execute, and a target to parse for. <br />
- file: text should be tagged according to `apertium-tagger -p -g`
- function: wordCount, lemmaCount, tagCount, wordsWithTag, lemmasWithTag, unanalyzedLemmas, multiwords_words, multiwords_lemmas'
- target: a tag, a word, or 0 depending on the function

**example usage:**

`python ./parser file.txt wordCount dogs` <br />
`python ./parser file.txt lemmaCount dog` <br />
`python ./parser file.txt tagCount n` <br />
`python ./parser file.txt wordsWithTag adj` <br />
`python ./parser file.txt lemmasWithTag vbmod` <br />
`python ./parser file.txt unanalyzedLemmas 0` <br />
`python ./parser file.txt multiwords_words 0` <br />
`python ./parser file.txt multiwords_lemmas 0` <br />

**available functions**

- **wordCount:** prints how many times the word appears in the file
- **lemmaCount:** prints how many times the lemma appears in the file
- **tagCount:** prints how many words in the file contain the tag
- **wordsWithTag:** prints a list of all the words that contain the tag, in alphabetical order
- **lemmasWithTag:** prints a list of all the lemmas that contain the tag, in alphabetical order
- **unanalyzedLemmas:** prints a list of all unanalyzed lemmas, in alphabetical order
- **multiwords_words:** prints a list of all multiwords in their word form, in alphabetical order
- **multiwords_lemmas:** prints a list of all multiwords in their lemma form, in alphabetical order

**extractor.py** challenge #3
================================
**Usage**:

`python ./extractor.py [input file] [output file]` <br />
Takes an input file, writes sentences containing discontiguous multiwords into an output file. <br />
Does not work well with documents including quotations.

**extractor_output.txt**
A sample document containing sentences with discontinuous multiwords. Created with `extractor.py` for `sample_texts/random_sentences.txt`. Manually marked to distinguish real discontinuous multiwords from non-real discontinuous multiwords. <br />


Contains those sentences from the output file of `sample_text/random_sentences.txt` that are found to contain discontiguous multiwords. The sentences are manually marked to distinguish between real discontiguous multiwords and non-real discontiguous multiwords. Real discontiguous multiwords are marked with `*` and non-real discontiguous multiwords are marked with `< >`.
