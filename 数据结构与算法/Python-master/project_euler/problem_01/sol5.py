'''
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.
'''
from __future__ import print_function
try:
    input = raw_input #python3
except NameError:
    pass               #python 2

"""A straightforward pythonic solution using list comprehension"""
n = int(input().strip())
print(sum([i for i in range(n) if i%3==0 or i%5==0]))

