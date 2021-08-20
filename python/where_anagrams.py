#!/usr/bin/python3

from eval_time import eval_time

def anagrams(word, words):
    # Add each word from the list whose reassembled version matches the reassembled version of the original word.
    return '' if not words else [w for w in words if ''.join(sorted(w)) == ''.join(sorted(word))]


eval_time(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
