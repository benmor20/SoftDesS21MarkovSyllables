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
    length = len(clean_word)
    for index in range(1,length):
        char = clean_word[index]
        if char not in letters:
            raise ValueError("Cannot have characters other than letters in " + \
                "provided word (word: " + clean_word + ")")
        if char in vowels:
            continue
        if index < length - 1 and clean_word[index:index+2] in consonant_pairs:
            continue
        syllables = [clean_word[:index+1]] + syllablize(clean_word[index+1:])
        if len(syllables[-1]) == 0:
            return syllables[:-1]
        return syllables
    return [clean_word]



!!!!!!DON"T FORGET TO SPLIT BY END OF END OF LIST!!!!



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
