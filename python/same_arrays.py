#!/usr/bin/python3

from eval_time import eval_time

def comp(array1, array2):
    if array1 is None or array2 is None:
        return False

    return sorted([ x ** 2 for x in array1 ]) == sorted(array2)


# Best practices

# Haven't dig deep enough in error handling, but try/except seems to fit ideally here

def comp_bp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

a1 = None
a2 = None

#a1 = []
#a2 = []

eval_time(comp(a1, a2))
