def syllablize(word):
    """
    Breaks a word up into syllables.

    Args:
        word: a string representing a single word to break up
    
    Returns:
        a list of strings, where wach string is one syllable, in order.
    """

    clean_word = preprocess(word)
    consonant_pairs = ("sh", "ph", "th", "ch", "wh", "tc", "ck") # tc is for tch
    vowels = "aeiouy"
    letters = "qwertyuiopasdfghjklzxcvbnm"
    length = len(word)
    for index in range(1,length):
        char = word[index]
        if char not in letters:
            raise ValueError("Cannot have characters other than letters in " + \
                "provided word (word: " + clean_word + ")")
        if char in vowels:
            continue
        if index < length - 1 and word[index:index+2] in consonant_pairs:
            continue
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
    remove = ".,/\\?!-'\"()\{\}[]:;"
    cleaned = word.lower()
    for punc in remove:
        cleaned = cleaned.replace(punc, "")
    return cleaned
