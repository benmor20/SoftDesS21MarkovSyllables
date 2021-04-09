"""
Apply Markov chain generation to a text, but with syllables
"""

import random
import syllablizer

def build_word_list(source_text):
    """
    Compiles source text into a list of words, preprocessing them. Will also
    remove anything it deems to not be words. These include tokens with digits,
    and tokens without any lowercase letters (aka abbreviations or tokens that
    are just symbols)

    Args:
        source_text: a string, the text to split into a word list

    Returns:
        A list of strings, where each string is a word in the source text that
            comply to the rules above. Each word is also preprocessed.
    """
    words = source_text.replace("\n", " ").split()
    # can't use isalpha because that includes accents, which syllablizer cannot deal with
    letters = "qwertyuiopasdfghjklzxcvbnm"
    digits = "1234567890"
    word_list = []
    for word in words:
        alpha = True
        has_lower = False
        # check that all except first and last are letters - first for (, {, [,
        # last for punc and closing
        for char in word[1:-1]:
            if char.lower() not in letters:
                alpha = False
                break
            if char == char.lower():
                has_lower = True
        if word[0] in digits or word[-1] in digits:
            continue
        if not alpha or not has_lower:
            continue
        if len(word) == 2 and word[0] not in letters and word[1] not in letters:
            continue
        if len(word) == 1 and word not in letters:
            continue
        clean = syllablizer.preprocess(word)
        if len(clean) > 0:
            word_list.append(clean)
    return word_list


def build_syllable_list(source_text):
    """
    Split a source text into syllables.

    Args:
        source_text: a string, the corpus to split into syllables.

    Returns:
        A list of lists of strings, where each sublist is a single word, and
            each string in the sublist is a single syllable.
    """
    return [syllablizer.syllablize(word) for word in build_word_list(source_text)]


def build_next_syllables(source_text):
    """
    Builds the dictionary of next syllables given a source text.

    Specifically, will map every syllable to each syllable that follows it,
    preserving frequency. Any syllable at the end of a word will include a
    mapping to an empty string. The first element of the resulting dict will
    map an empty string to a list of all syllables that start the word.

    Args:
        source_text: a string, the corpus ot build the syllable mapping for.

    Returns:
        A dict mapping strings (syllables) to lists of strings (all syllables
            that follow the key) as per the rules above.
    """
    syll_list = build_syllable_list(source_text)
    output_dictionary = {"": []}

    for word in syll_list:
    #    if len(word) == 1:
    #        continue
        output_dictionary[""].append(word[0])
        sylls = word + [""]
        for syll_index, syll in enumerate(sylls[:-1]):
            next_sylls = output_dictionary.setdefault(syll, [])
            next_sylls.append(sylls[syll_index + 1])
            #output_dictionary[syll] = next_sylls
    return output_dictionary



def generate_word(next_sylls):
    """
    Generates a single word given a syllable mapping from build_next_syllables.

    Specifically, will choose a random element from the list of syllables for
    an empty string, and append that to a string. Will then choose a random
    element from the last syllable chosen and append that to the end of the
    string, repeating until an empty string is chosen.

    Args:
        next_sylls: a dictionary of strings to lists of strings, representing
            all syllables and the list of all syllables that follow it in a
            certain corpus.

    Returns:
        A string representing a random word generated from running a Markov
            chain on next_sylls, as per the specification above.
    """
    word = ""
    syll = random.choice(next_sylls[""])
    while len(syll) > 0:
        word += syll
        syll = random.choice(next_sylls[syll])
    return word
