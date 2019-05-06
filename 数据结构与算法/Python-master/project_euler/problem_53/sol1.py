#-.- coding: latin-1 -.-
from __future__ import print_function
from math import factorial
'''
Combinatoric selections
Problem 53

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n!/(r!(n−r)!),where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of nCr, for 1 ≤ n ≤ 100, are greater than one-million?
'''
try:
	xrange		#Python 2
except NameError:
	xrange = range	#Python 3

def combinations(n, r):
	return factorial(n)/(factorial(r)*factorial(n-r))

total = 0

for i in xrange(1, 101):
	for j in xrange(1, i+1):
		if combinations(i, j) > 1e6:
			total += 1

print(total)