import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from get_text import get_texts
from get_text import books

def tokenize(text):
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
    books = book
    is_list = type(book) is list
    if not is_list:
        books = [book]
    all_tokens = {}
    for book in books:
        response = tfidf.transform([texts[book]])
        tokens = {}
        for index in response.nonzero()[1]:
            tokens[feature_names[index]] = response[0, index]
        all_tokens[book] = tokens
    return all_tokens if is_list else all_tokens[book]


def num_nonzero_tokens(book):
    tokens = nonzero_tokens(book)
    if type(book) is list:
        num_tokens = []
        for index,title in enumerate(book):
            num_tokens.append(len(tokens[title]))
        return num_tokens
    return len(tokens)
