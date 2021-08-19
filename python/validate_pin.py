#!/usr/bin/python3

from time import time

def validate_pin(pin):
    validated = len([x for x in pin if x in '0123456789'])
    return True if validated in [4, 6] and validated == len(pin) else False


# better

def validate_pin_improved(pin):
    return len(pin) in (4, 6) and pin.isdigit()


pin = '10056'
pin = '100564'
pin = '-100564'
#pin = '100f64'
#pin = '1064'

def eval_time(func):
    from time import time
    start = time()
    print(func)
    #func
    end = time()
    print(end - start)

#print(validate_pin(pin))
eval_time(validate_pin(pin))

#print(validate_pin_improved(pin))
eval_time(validate_pin_improved(pin))


def my_tuple(num):
    return num in (3, 5)

def my_list(num):
    return num in [3, 5]

def my_string(string):
    return string in '35'

eval_time(my_tuple(3))
eval_time(my_list(3))
eval_time(my_string('3'))
