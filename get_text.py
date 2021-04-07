"""Contains code to handle the downloading of texts and performing preliminary formatting."""

from urllib import request
import markov_with_syllables as markov
import syllablizer
import validators

books = {
    "Iliad": "http://www.gutenberg.org/files/6150/6150-0.txt",
    "Canterbury Tales": "http://www.gutenberg.org/cache/epub/2383/pg2383.txt",
    "Romeo and Juliet": "http://www.gutenberg.org/ebooks/1777.txt.utf-8",
    "Great Gatsby": "http://www.gutenberg.org/files/64317/64317-0.txt",
    "Monty Python": "https://raw.githubusercontent.com/teropa/nlp/master/resources/corpora/webtext/grail.txt",
    "Finnegan's Wake": "https://archive.org/stream/finneganswake00joycuoft/finneganswake00joycuoft_djvu.txt",
    }

def web_scrape(url):
    """
    Performs a simple web scrape for a URL referencing a text file.
    
    Args:
        Book: a string representing a URL that points to a utf-8 text.
        file.
    
    Returns:
        A string of the entire text of the file.
    """
    response = request.urlopen(url)
    text = response.read().decode("utf8")
    return text

def get_texts(book):
    """
    Gets the text from a dictionary of corpus.
    
    Args:
        book: a string representing a URL pointing to a UTF-8 text file or
        a book name in the included dictionary, or "all".
        
    Returns:
        A dictionary containing the text's name as a key
    """
    all_texts = {}
    if book in books:
        text = web_scrape(books[book])
        return text
    elif validators.url(book) == True:
        text = web_scrape(book)
        return text
    elif book == "all":
        for book in books:
            all_texts[book] = web_scrape(books[book])
        return all_texts
    else:
        raise Exception(f"That wasn't a key. Your options are {books.keys()}")
        
def add_text(url, initial_dictionary={}, text_name="use_url"):
    """
    Given a dictionary of texts and a URL of a UTF-8 text, adds that text to
    the dictionary and returns the dictionary.
    
    Args:
        url: A string representing a URL that references a text file in UTF-8.
        initial_dictionary: the initial dictionary to add a text to.
        text_name: (optional) if given, this string specifies the dictionary
            key that the text is stored under.

    Returns:
        The input dictionary with the text from the URL included at the
    end of that dictionary, under the key specified by text_name, or the given
    URL if text_name was not given.
    """
    new_text_key = url
    if validators.url(url) == True:
        new_corpus = web_scrape(url)
        if text_name != "use_url":
            new_text_key = text_name
    elif url in books:
        new_corpus=web_scrape(books[url])
    initial_dictionary[new_text_key] = new_corpus
    return initial_dictionary