def syllablize(word):
    """
    Breaks a word up into syllables.

    Args:
        word: a string representing a single word to break up
    
    Returns:
        a list of strings, where wach string is one syllable, in order.
    """
    consonant_pairs = ("sh", "ph", "th", "ch", "wh", "tc", "ck", "nd", "gh") # tc is for tch
    vowels = "aeiouy"
    letters = "qwertyuiopasdfghjklzxcvbnm"
    length = len(word)
    for index in range(1,length):
        char = word[index]
        if char not in letters:
            raise ValueError("Cannot have characters other than letters in " + \
                "provided word (word: " + word + ")")
        if index == 1 and word[0:2] in consonant_pairs:
            continue
        if char in vowels:
            continue
        if index < length - 1 and word[index:index+2] in consonant_pairs:
            continue
        if word[index+1:] == "e" or (index + 2 == length and word[index+1:] not in vowels): # silent e and consontant pairs like at the end of should
            return [word]
        syllables = [word[:index+1]] + syllablize(word[index+1:])
        if len(syllables[-1]) == 0:
            return syllables[:-1]
        return syllables
    return [word]


def preprocess(word):
    """
    Preprocesses a word.

    Specifically, runs lower and remove punctuation

    Args:
        word: a string to preprocess. Assumed to be a single word.
    
    Returns:
        A string representing the cleaned version of the word
    """
    letters = "qwertyuiopasdfghjklzxcvbnm"
    smol = word.lower()
    cleaned = ""
    for letter in smol:
        if letter in letters:
            cleaned += letter
    return cleaned
