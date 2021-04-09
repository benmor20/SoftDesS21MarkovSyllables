"""
Test that the markov generator works properly.
"""
import markov_with_syllables as markov

WORD_LIST_CASES = [
    ("This is an example sentence", ['this', "example", "sentence"]),
    ("4 score and 7 years ago", ['score', 'and', "years", "ago"]),
    ("The NBA is an abbreviation", ['the', "abbreviation"]),
    ("Yes, are you?", ['yes', "are", "you"]),
]

SYLL_LIST_CASES = [
    ("This is an example sentence", [['this'], ['e', 'xam', 'ple'], ['sen', 'ten', 'ce']]),
    ("4 score and 7 years ago", [['s', 'core'], ['and'], ["years"], ["a", "go"]]),
    ("The NBA is an abbreviation", [['the'], ["ab", "b", "re", "via", "tion"]]),
    ("Yes, are you?", [['yes'], ["are"], ["you"]]),
]

NEXT_SYLL_CASES = [
    ("This is an example sentence", {'': ['this', 'e', 'sen'], 'this': [''], 'e': ['xam'],
    'xam': ['ple'], 'ple': [''], 'sen': ['ten'], 'ten': ['ce'], 'ce': ['']}),
    ("4 score and 7 years ago", {'': ['s', 'and', 'years', 'a'], 's': ['core'], 'core': [''],
    'and': [''], 'years': [''], 'a': ['go'], 'go': ['']}),
    ("The NBA is an abbreviation", {'': ['the', 'ab'], 'the': [''], 'ab': ['b'], 'b': ['re'],
    're': ['via'], 'via': ['tion'], 'tion': ['']}),
    ("Yes, are you?", {'': ['yes', 'are', 'you'], 'yes': [''], 'are': [''], 'you': ['']}),
    ("We almost always chose video games when allowed", {'': ['al', 'al', 'chose', 'vi', 'ga',
    'when', 'al'], 'al': ['most', 'ways', 'lo'], 'most': [''], 'ways': [''], 'chose': [''],
    'vi': ['deo'], 'deo': [''], 'ga': ['mes'], 'mes': [''], 'when': [''], 'lo': ['wed'],
    'wed': ['']})
]

def test_word_list():
    """
    Tests markov.build_word_list
    """
    for case in WORD_LIST_CASES:
        assert markov.build_word_list(case[0]) == case[1]


def test_syll_list():
    """
    Tests markov.build_syllable_list
    """
    for case in SYLL_LIST_CASES:
        assert markov.build_syllable_list(case[0]) == case[1]


def test_next_sylls():
    """
    Tests markov.build_next_syllables
    """
    for case in NEXT_SYLL_CASES:
        assert markov.build_next_syllables(case[0]) == case[1]
