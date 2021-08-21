#!/usr/bin/python3

# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
# 
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

from eval_time import eval_time

def count_bits(n):
    return sum(int(x) for x in bin(n)[2:])


# Better
# Why don't we just count number of character occurrences in a string, indeed.

def count_bits_impr(n):
    return bin(n).count("1")



eval_time(count_bits(50235))
