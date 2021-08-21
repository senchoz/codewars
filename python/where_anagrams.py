#!/usr/bin/python3

from eval_time import eval_time

def anagrams(word, words):
    # Add each word from the list whose reassembled version matches the reassembled version of the original word.
    return '' if not words else [w for w in words if ''.join(sorted(w)) == ''.join(sorted(word))]




# Improvement
# Why join list of letters to a word if we can compare the lists itself :)

def anagrams_impr(word, words):
    # Add each word from the list whose sorted vowels list matches the same of the original word.
    return '' if not words else [w for w in words if sorted(w) == sorted(word)]


eval_time(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
eval_time(anagrams_impr('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
