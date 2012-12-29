"""
Week 4 Notes
Chapter 2
"""

from operator import getitem
from fractions import gcd

# 2.2 Data Abstraction

def rational(n, d):
	g = gcd(n, d)
	return n//g, d//g

def numer(x):
	return getitem(x, 0)

def denom(x):
	return getitem(x, 1)

def add_rationals(x, y):
	nx, dx = numer(x), denom(x)
	ny, dy = numer(y), denom(y)
	return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
	return rational(numer(x) * numer(y), denom(x) * denom(y))

def eq_rationals(x, y):
	return numer(x) * denom(y) == numer(y) * denom(x)

# 2.3 Sequences of Data

empty_rlist = None

def rlist(first, rest):
	return (first, rest)

def first(s):
	return s[0]

def rest(s):
	return s[1]

def len_rlist(s):
	n = 0
	while rest(s) is not None:
		s, n = rest(s), n + 1
	return n

def getitem_rlist(s, i):
	while i > 0:
		s, i = rest(s), i - 1
	return first(s)

