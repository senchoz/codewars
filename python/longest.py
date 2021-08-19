#!/usr/bin/python3

from string import ascii_lowercase
from eval_time import eval_time

def longest(a1, a2):
    return ''.join([c for c in ascii_lowercase if c in a1 + a2])


# better
# doesn't require string import
# set naturally makes sure we have only unique values, so only sorting is left

def longest_improved(a1, a2):
    return ''.join(sorted(set(a1 + a2)))

a = "xyaabbbccccdefwwwhatever the string is"
b = "xxxxyyyyabklmopq"

eval_time(longest(a, b), 10**7)
eval_time(longest_improved(a, b), 10**7)
