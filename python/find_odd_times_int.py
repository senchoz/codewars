#!/usr/bin/python3

from eval_time import eval_time

# Given an array of integers, find the one that appears an odd number of times.
# 
# There will always be only one integer that appears an odd number of times.
# 
# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] shold return 4, because it appears 1 time (which is odd).


#
# 2 for loops
# parent loop iterates over the remaining list
# child loop finds and removes occurrences of the last element in sequence and increments the counter
# or just appends the values to temp list so later we can evaluate list lenght
# on next parent loop iteration temp list gets overwritten

seq = [20,1,-1,2,-2,3,3,3,5,5,1,2,4,20,4,-1,-2]


def find_it(seq):
    # by task we have an non-empty array
    # we will iterate until we found a number occurring odd number of time
    # while elements in seq is still there
    tmp_seq = seq[:]
    while tmp_seq:
        # pop the last element in list and count it as 1st occurrence
        last, count = tmp_seq.pop(), 1
        
        # while the popped element is still in sequence acknowledge this by incrementing occurence counter 
        # and remove its next occurence from the sequence (looking from left to right)
        while last in tmp_seq:
            count += 1
            tmp_seq.remove(last)
        
        # once all occurrences of the popped element were removed from the sequence,
        # return popped element if it appears odd number of times
        # or proceed with next iterations until the element that appears odd number of times is found.
        if count % 2 == 1:
            return last


# best practices
def find_it_bp(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

eval_time(find_it(seq), 10 ** 6)
eval_time(find_it_bp(seq), 10 ** 6)

