#!/usr/bin/python3

from eval_time import eval_time

x = 371

def narcissistic( value ):
    return True if sum([int(x) ** len(str(value)) for x in str(value)]) == value else False

eval_time(narcissistic(x))
eval_time(narcissistic(x))


# better
# there is no need to specify bool value explicitly as it will be returned once expression is evaluated 

def narcissistic(value):
        return value == sum(int(x) ** len(str(value)) for x in str(value))
