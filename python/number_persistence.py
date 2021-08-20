#!/usr/bin/python3

# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
# 
# For example:
# 
#  persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
#                  # and 4 has only one digit
#                   
#  persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
#                   # 1*2*6=12, and finally 1*2=2
# 
#  persistence(4) # returns 0, because 4 is already a one-digit number


from eval_time import eval_time

# Takes number as an input and returns the product of its digits
# Recursion was used. We take 1st digit and multiply it by the product of the rest

def product(n):
    #print(f"n = {n} returned")
    #print(f"Calculating product")
    print(f"n = {n} passed")
    if len(str(n)) > 1:
        if '0' in str(n):
            print(f"Number contains 0. Returning 0")
            return 0
        #print(f"int(str(n)[0]) = {int(str(n)[0])}")
        #print(f"mult1 = {int(str(n)[0])}")
        mult1 = int(str(n)[0])
        mult2 = product(int(str(n)[1:]))
        prod = mult1 * mult2
        print(f"{mult1} * {mult2} = {prod}")

        #print(f"product(int(str(n)[1:])) = {product(int(str(n)[1:]))}")
        #print(f"mult2 = {product(int(str(n)[1:]))}")
        #print(f"int(str(n)[0]) * product(int(str(n)[1:])) = {int(str(n)[0]) * product(int(str(n)[1:]))}")
        #return int(str(n)[-1]) * product(int(str(n)[0:-1]))
        #print(f"returning mult1 * mult2")
        #return int(str(n)[0]) * product(int(str(n)[1:]))
        print(f"Returning {prod} and getting 1 level higher")
        return prod
    else:
        print(f"n = {n}, deepest n returned")
        print(f"Starting a path from recursion")
        return n

# Checks 

def persistence(n):
    print("start persistence function")
    depth = 0
    #while len(str(n)) > 1:
    try:
        while n > 9:  # also possible, while n is larger than largest digit
            print(f"n = {n}")
            print(f"depth = {depth}")
            print(f"Reducing number n by calling 'product(n)'")
            n = product(n)
            print(f"n reduced to {n}")
            print("Incrementing depth")
            depth += 1
        print(f"Number is a digit, returning depth = {depth}")
        return depth
    except:
        print("Error: Argument must be an instance of 'int'")
        return -1



# Most popular

from functools import reduce
import operator
def persistence_imp(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

#eval_time(persistence(11))
#eval_time(persistence(100021))
#eval_time(persistence(468299))
eval_time(persistence(468297))
eval_time(persistence_imp(468297))
#eval_time(persistence('11'))
#eval_time(persistence(None))
