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
    response = tfidf.transform([texts[book]])
    tokens = {}
    for index in response.nonzero()[1]:
        tokens[feature_names[index]] = response[0, index]
    return tokens


for book in books:
    print(f"{book}: {len(nonzero_tokens(book))}")
