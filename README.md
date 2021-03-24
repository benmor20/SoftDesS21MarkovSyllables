# Markov Syllables
A project by Ben Morris and CJ Hilty

## Purpose
This is a repository to support a python project that explores the syllable structure of words in english. Our hypothesis is: **Voluneers can make sense of computer-combined syllables to the point of at least proposing definitions.**

## Overview
We built a [Discrete-Chain Markov Generator](https://en.wikipedia.org/wiki/Discrete-time_Markov_chain) for a text source, which will split every word by syllable, and build words based on the syllables that most commonly occur after each syllable in the source. 

## Data Sources
We are using the Wikipedia article to run our markov generator on the text of the top 5 english wikipedia articles.

<!--- Add additional data sources here as we go -->
