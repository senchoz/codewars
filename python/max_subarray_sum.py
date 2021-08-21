#!/usr/bin/python3

# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
# 
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
# 
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

from eval_time import eval_time


#eval_time(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

def max_sequence(arr):
    d = {k: v for (k, v) in [(sum(arr[i:]), arr[i:]) for i in range(len(arr)+1)]}
    for k, v in d.items(): #
        print(k, v) #
    #print(d)
    arr = d[max(d.keys())]
    print(f"first processed arr {arr}")
    d = {k: v for (k, v) in [(sum(arr[:i]), arr[:i]) for i in range(len(arr)+1)]}
    print(d)
    arr = d[max(d.keys())]
    print(arr)
    return arr

def max_sequence_sum(arr):
    d = {k: v for (k, v) in [(sum(arr[i:]), arr[i:]) for i in range(len(arr))]}
    arr = d[max(d.keys())]
    return max([sum(arr[:i]) for i in range(len(arr))])



#eval_time(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 45]))
#eval_time(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 6]))
#eval_time(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, -5, -5, -5, -5, -5, -5, 20]))
#eval_time(max_sequence_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
#eval_time(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, -5, -5, -5, -5, -5, -5, 20]))
#eval_time(max_sequence([-2, 1, -3, 4, -1, 3, -35, 20]))

arr = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]
#arr = [-6, 7, 28, 1, 16, -1, 1, 5, -5, 14, 21, 19, -27, 11, 0, 1, -21, -22, -29, 10, -2, 30, 21, 9, -21, 30, -16, 27, -9, 16, -5, -12, 8, -25, 3, -21, 7, -25, -12, -22, 14, 1, 12, -27, -1, -22, -25, 18, -28, 16]

arr = [-6, 13, 12, -3, -14, -27, -17, -15, 26, 23, -8, 27, -28, -15, 3, -4, 15, -25, 3, 23, -17, -2, -13, 26, -30, 4, -8, -30, -20, -15, -12, -15, 3, -7, 30, 7, 11, -14, -21, -15, -14, -7, -30, -14, -5, -21, -8, 27, -13, 28] # should be [26, 23, -8, 27] = 68

#eval_time(max_sequence_sum(arr))
#eval_time(max_sequence(arr))


def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = 0  # or: float('-inf')
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


eval_time(max_subarray(arr))
