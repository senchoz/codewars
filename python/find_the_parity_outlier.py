#!/usr/bin/python3

number = [2, 4, 6, 8, 10, 3]
number_list = [2, 4, 5]
number_list = [160, 3, 1719, 19, 11, 13, -21]

def find_outlier(number_list):
    is_odd = 1 if sum([ number_list[i] % 2 for i in range(3) ]) > 1 else 0
    return [ number for number in number_list if number % 2 != is_odd ][0]

print(find_outlier(number_list))
