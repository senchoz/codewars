#!/usr/bin/python3

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
# 
# For example:
# 
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

from eval_time import eval_time

def unique_in_order(iterable):
    last = ''
    result = []
    for c in iterable:
        if str(c) != last: result.append(c)
        last = str(c)
    return result



eval_time(unique_in_order('AAAABBBCCDAABBB')) #== ['A', 'B', 'C', 'D', 'A', 'B']
eval_time(unique_in_order('ABBCcAD'))         #== ['A', 'B', 'C', 'c', 'A', 'D']
eval_time(unique_in_order([1,2,2,3,3]))       #== [1,2,3]
