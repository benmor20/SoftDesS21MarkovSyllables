# Markov Syllables
*A project by Ben Morris and CJ Hilty*

## Purpose
This is a repository to support a python project that explores the syllable structure of words in English. Our hypothesis is: **Given an English corpus, a computer can replicate English words that it has not yet seen using a Discrete-Chain Markov Generator.**

## Overview
### Syllablizer
We first built a syllablizer based off the instructions at [this link](https://archive.org/details/finneganswake00joycuoft/?view=theater). It splits the syllables around consonants (keeping consonant pairs like `ch` and `wh` together). If there are two consonants, it splits between them. If one, it splits after. If all that is left in the word after the split are consonants, it will append it to the end of the word. While we know this method is not perfect, we figured it would be good enough for our purposes. Plus, we could not code in *all* the exceptions.

### Markov Generator
The next step was to code the [Discrete-Chain Markov Generator](https://en.wikipedia.org/wiki/Discrete-time_Markov_chain). After cleaning up and syllablizing the whole text, we generate a mapping of each syllable to a list of all possible syllables that follow it, maintaining frequency. To generate a word, we select a random syllable from a list that start words, then choose a random syllable that follows it, then one that follows that, and so on, until we choose an empty string, which means "end word". To see the results of this, along with some more detail on our process, see our computational essay. 

## Data Sources
We are using a variety of popular texts throughout time as our corpora - a complete list (along with their sources) is below.

* The Iliad ([Project Gutenberg](https://www.gutenberg.org/))
* Romeo and Juliet ([Project Gutenberg](https://www.gutenberg.org/))
* The Canterbury Tales ([Project Gutenberg](https://www.gutenberg.org/))
* The Great Gatsby ([Project Gutenberg](https://www.gutenberg.org/))
* Monty Python and the Holy Grail ([Teropa's NLP GitHub](https://github.com/teropa/nlp/tree/master/resources/corpora/webtext))
* Finnegan's Wake ([archive.org](https://archive.org))

The exact links to each text files can be seen in `get_text.py`

The other source for our data was a Google Form we sent out to the members of Olin College and [r/SampleSize](https://reddit.com/r/SampleSize), along with some of our friends we knew outside of these communities. This form asked participants to define a small sample of the words we generated. While we did not have time to do extensive analysis on this data, the data we did compile can be seen on this [Google Sheet](https://docs.google.com/spreadsheets/d/1RYumooRb3sfSeXJ3BsLNq-STmKJLvugCud32MD103hw/edit?usp=sharing).

## Setup
To setup this project to run properly, you will need to run the following commands:
```
$ pip install matplotlib
$ pip install numpy
$ pip install sklearn
$ pip install urllib
$ pip install validators
$ pip install nltk
$ python
    >> nltk.download("words")
    >> nltk.download("punkt")
```
