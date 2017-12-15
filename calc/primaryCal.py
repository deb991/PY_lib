#!/usr/bin/env python
import os
import math
from math import sqrt
import random
import cmath

#Basic Calculation for numerical operations.

num = int(input('Input the number:: '))

def PON():      #PON: Prime or, Not.
    if num > 1:
        for i in range(2, num):
            if (num % 2) == 0:
                print("Mentioned number isn't a prime: ", num)
                break
            else:
                print("Mentioned number is a prime number: ", num)

def root():     #Compatiable with Python 3.x distribution.
    root_val = math.sqrt(num)
    print(root_val)

def root4all():
    rt_vl = num**(1/2)
    print(rt_vl, 'This is based on most compatiable method for all Python Distributions. ')

def sqr():
    sqr_val = num*num
    print(sqr_val)

if __name__ == '__main__':
    PON()
    root()
    root4all()
    sqr()
