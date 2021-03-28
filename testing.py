"""import google_books.googlebooks as gb

api = gb.Api()
books = api.list('intitle:"Romeo and Juliet"')["items"]
for book in books:
    if book["accessInfo"]["publicDomain"]:
        isbn = book["volumeInfo"]["industryIdentifiers"][0]["identifier"]
        for isbn_info in book["volumeInfo"]["industryIdentifiers"]:
            if isbn_info["type"] == "ISBN_13":
                isbn = isbn_info["identifier"]
                break
        print(book["volumeInfo"]["title"] + " (" + isbn + ")")

ranj = api.list("idbn:HARVARD:HNL9UV")"""

from urllib import request
import markov_with_syllables as markov
import syllablizer

books = {
    "Romeo and Juliet": "http://www.gutenberg.org/ebooks/1777.txt.utf-8",
    "Finnegan's Wake": "https://archive.org/stream/finneganswake00joycuoft/finneganswake00joycuoft_djvu.txt",
    "Great Gatsby": "http://www.gutenberg.org/files/64317/64317-0.txt",
    "Canterbury Tales": "http://www.gutenberg.org/cache/epub/2383/pg2383.txt",
    "Iliad": "http://www.gutenberg.org/files/6150/6150-0.txt",
    "Monty Python": "https://raw.githubusercontent.com/teropa/nlp/master/resources/corpora/webtext/grail.txt"
}
response = request.urlopen(books["Monty Python"])
text = response.read().decode("utf8")

MAX_WORDS = 10000
sylls = markov.build_next_syllables(text)
all_words = set(markov.build_word_list(text))
num_words = 0
novel_words = set()
words = set()
while num_words < MAX_WORDS:
    word = markov.generate_word(sylls)
    if len(syllablizer.syllablize(word)) > 1:
        words.add(word)
        if word not in all_words:
            novel_words.add(word)
        num_words += 1
print(f"Generated {MAX_WORDS} words, {len(words)} of which were unique.")
print(f"Of the unique words, {len(novel_words)} are new and {len(words) - len(novel_words)} are from the text")
print("10 novel words:")
for _ in range(10):
    print(novel_words.pop())
