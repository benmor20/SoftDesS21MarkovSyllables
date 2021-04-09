"""
Test that the syllable splitter works properly.
"""

from syllablizer import (
    preprocess,
    syllablize
)

WORD_CASES = [
    #Test Words of varying syllables -
    ("apple", ['ap', 'ple']),
    ("passive", ['pas', 'sive']),
    ("influential", ['in', 'f', 'luen', 'tial']),
    ("provisions", ['p', 'ro', 'vi', 'sions']),
    ("partners", ['par', 't', 'ners']),
    ("bluebell", ['b', 'lue', 'bell']),
    ("rationale", ['ra', 'tio', 'nale']),
    ("account", ['ac', 'count']),
    ("banana", ['ba', 'na', 'na']),
    ("tiny", ['ti', 'ny']),
    ("draft", ['d', 'raft']),
    ("student", ['s', 'tu', 'dent']),
    ("flakes", ['f', 'la', 'kes']),
    ("concrete", ['con', 'c', 'rete']),
    ("described", ['des', 'c', 'ri', 'bed']),
    ("recognition", ['re', 'cog', 'ni', 'tion']),
    ("niche", ['niche']),
    ("condominiums", ['con', 'do', 'mi', 'niums']),
    ("recorded", ['re', 'cor', 'ded']),
    ("September", ['sep', 'tem', 'ber']),
    ("ceremony", ['ce', 're', 'mo', 'ny']),
    #Test some capitalized words
    ("Africa", ['af', 'ri', 'ca']),
    ("Olin", ['o', 'lin']),
    #Test some hyphenated words
    ("Check-in", ['chec', 'kin']),
    ("Coca-Cola", ['co', 'ca', 'co', 'la']),
]


def test_syllablizer():
    """
    Tests syllaiblizer function
    """
    for case in WORD_CASES:
        assert syllablize(preprocess(case[0])) == case[1]
