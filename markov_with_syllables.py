import syllablizer

def build_syllable_list(source_text):
    """
    Split an input into a list of the source's "words" based on whitespace.
    If the separated "words" contain punctuation, the punctuation will be
    preserved, but spaces and other whitespace are removed.
    """

    words = source_text.split()
    words = [word for word in words if syllablizer.preprocess(word).isalpha()]

    syllables = []

    return [syllablizer.syllablize(word) for word in words]


def build_next_words(word_list):
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
    sentence_end_punctuation = ['?', '!', '.']
    output_dictionary = {}
    

    for index, word in enumerate(word_list):
        if word[-1] in sentence_end_punctuation:
            output_dictionary[word] = [""]
        elif word not in output_dictionary:
            if index + 1 < len(word_list):
                output_dictionary[word] = [word_list[index + 1]]
        else:
            if index + 1 < len(word_list):
                output_dictionary[word].append(word_list[index + 1])
        if index == 0:
            output_dictionary[""] = [word]
        elif word_list[index - 1][-1] in sentence_end_punctuation:
            output_dictionary[""].append(word_list[index])
    return output_dictionary



def generate_sentence(next_words):
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
    sentence = ""
    word = ""
    word = random.choice(next_words[''])
    # while next_words[key] != ['']:
    while "" not in next_words[word]:
        next_word = random.choice(next_words[word])
        sentence = sentence + word + " "
        word = next_word
    sentence = sentence + word
    return sentence


def generate_text(next_words, num_sentences):
    """
    Generates multiple sentences by running the generate_sentence function
    multiple times and concatenating the results.

    Args: next_words, a dictionary that contains words that come next in
    a starter text, and words that start sentences stored under the entry
    for "".
    num_sentences, a positive integer that tells the function how many
    sentences to generate.

    Returns: A string with the specified number of sentences.

    """

    paragraph = ""
    for _ in range(num_sentences):
        paragraph = paragraph + generate_sentence(next_words) + " "
    return paragraph[:-1]

with open("jabberwocky.txt", "r") as file:
    source = file.read().replace("\n"," ")
print(build_syllable_list(source))