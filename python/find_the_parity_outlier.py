#!/usr/bin/python3

from time import time
from random import randint

number = [2, 4, 6, 8, 10, 3]
number_list = [2, 4, 5]
#number_list = [160, 3, 1719, 19, 11, 13, -21]
num = [ randint(1, 100) for i in range(30000) ]
num_odd = [ x for x in num if x % 2 != 0]
num_even = [ x for x in num if x % 2 == 0]



number_list = num_odd + [2]
#number_list = num_even + [3]

def find_outlier(number_list):
    is_odd = 1 if sum([ number_list[i] % 2 for i in range(3) ]) > 1 else 0
    return [ number for number in number_list if number % 2 != is_odd ][0]

start = time()
print(find_outlier(number_list))
end = time()
print(end - start)


def find_outlier2(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

start = time()
print(find_outlier2(number_list))
end = time()
print(end - start)



start = time()
print(sum(num))
end = time()
print(end - start)

start = time()
print(sum(num[:2]))
end = time()
print(end - start)

