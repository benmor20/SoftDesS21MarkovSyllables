import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from get_text import get_texts
from get_text import books

def tokenize(text):
    """
    Tokenizes the given input text, and stems the result.

    Args:
        text: a string representing a corpus to tokenize.

    Returns:
        A list of stems of the tokens

    Code adapted from:
    https://www.bogotobogo.com/python/NLTK/tf_idf_with_scikit-learn_NLTK.php
    """
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems


texts = get_texts("all")
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(texts.values())
feature_names = tfidf.get_feature_names()

def nonzero_tokens(book):
    """
    Finds all tokens in the given corpus that have a nonzero TF/IDF value,
    along with their corresponding TF/IDF value when compared to all tokens in
    get_texts.

    Args:
        book: a string giving the title of the corpus to find tokens for, as
            defined in get_texts.py. Alternatively, a list of strings, giving
            titles for a list of corpora to find tokens for.
    
    Returns:
        A dictionary of strings to floats, mapping tokens in the specified
            corpus to their TF/IDF value. Alternatively, if book is a list of
            strings, will return a dictionary of book titles given in book to
            a dictionary of tokens (strings) to TF/IDF values (floats), as if
            a single title was given.

    Code adapted from:
    https://www.bogotobogo.com/python/NLTK/tf_idf_with_scikit-learn_NLTK.php
    """
    books = book
    is_list = type(book) is list
    if not is_list:
        books = [book]
    all_tokens = {}
    for index, book in enumerate(books):
        print(f"Starting TF/IDF of Text {index+1}/{len(books)}")
        response = tfidf.transform([texts[book]])
        tokens = {}
        for index in response.nonzero()[1]:
            tokens[feature_names[index]] = response[0, index]
        all_tokens[book] = tokens
    return all_tokens if is_list else all_tokens[book]


def num_nonzero_tokens(book):
    """
    Finds the number of tokens in the given corpus/corpora which have a nonzero
    TF/IDF value.

    Args:
        book: a string giving the title of the corpus to find the number of
            nonzero for, as defined in get_texts.py. Alternatively, a list of
            strings, giving titles for a list of corpora to find the number of
            nonzero tokens for.

    Returns:
        An integer, the number of tokens in the given corpus which have a
            nonzero TF/IDF value. Alternatively, if book is a list of strings,
            gives a list of integers as if this function was run on each of
            them.
    """
    tokens = nonzero_tokens(book)
    if type(book) is list:
        num_tokens = []
        for title in book:
            num_tokens.append(len(tokens[title]))
        return num_tokens
    return len(tokens)
