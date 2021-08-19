#!/usr/bin/python3

def eval_time(func, iterations = 1):
    from time import time
    start = time()
    for i in range(iterations):
        #print(func)
        func
    end = time()
    print(func)
    print((end - start))
    #print((end - start) / iterations)

