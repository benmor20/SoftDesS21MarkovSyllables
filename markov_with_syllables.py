import syllablizer
import random
import wikipedia

def build_word_list(source_text):
    words = source_text.replace("\n", " ").split()
    letters = "qwertyuiopasdfghjklzxcvbnm" # can't use isalpha because that includes accents, which syllablizer cannot deal with
    word_list = []
    for word in words:
        alpha = True
        has_lower = False
        for char in word[1:-1]: # check that all except first and last are letters - first for (, {, [, last for punc and closing
            if char.lower() not in letters:
                alpha = False
                break
            if char == char.lower():
                has_lower = True
        if not alpha or not has_lower:
            continue
        if len(word) == 2 and word[0] not in letters and word[1] not in letters:
            continue
        if len(word) == 1 and word not in letters:
            continue
        word_list.append(word)
    return word_list


def build_syllable_list(source_text):
    """
    Split an input into a list of the source's "words" based on whitespace.
    If the separated "words" contain punctuation, the punctuation will be
    preserved, but spaces and other whitespace are removed.
    """
    return [syllablizer.syllablize(word) for word in build_word_list(source_text)]


def build_next_syllables(source_text):
    """
    Creates a dictionary that, for every unique "word" (aka unique combination
    of characters) in a list of words, stores the "next word" in the list. If
    that "word" has a sentence-ending punctuation on it, then "" is added as
    the "next word" for that word's entry, and the next word will be stored in
    an entry for "".

    Args: word_list, a list of words that can include punctuation.
    word_list should not include whitespace.

    Returns: a dictionary with an entry for "" and an entry for each word in
    word_list. The entry for "" will contain each word that follows an end
    punctuation, while the entry for each word will contain the word that
    follows it in word_list. The entry for with end punctuation will be "".

    """
    syll_list = build_syllable_list(source_text)
    output_dictionary = {"": []}

    for word in syll_list:
        if len(word) == 1:
            continue
        output_dictionary[""].append(word[0])
        sylls = word + [""]
        for syll_index, syll in enumerate(sylls[:-1]):
            next_sylls = output_dictionary.setdefault(syll, [])
            next_sylls.append(sylls[syll_index + 1])
            #output_dictionary[syll] = next_sylls
    return output_dictionary



def generate_word(next_sylls):
    """
    Generates a random sentence by selecting a single sentence-starting
    word and several words from the dictionary next_words, then ends with
    a sentence-ending word. This type of generation uses markov chains, so
    we can call it a markov text generator.

    Args: next_words, a dictionary that contains words that come next in
    a starter text, and words that start sentences stored under the entry
    for "".

    Returns: A string that contains exactly one sentence built with words
    that appear after the previous word in an original text.

    """
    word = ""
    syll = random.choice(next_sylls[""])
    while len(syll) > 0:
        word += syll
        syll = random.choice(next_sylls[syll])
    return word


content = wikipedia.page("United States of America").content
print(generate_word(build_next_syllables(content)))