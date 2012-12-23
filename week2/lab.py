"""
CS61A
Week 2 Lab
"""

# Exercise 6
def max(a, b):
	"""
	Returns maximum of a, b

	>>> max(3, 4)
	4
	>>> max(2, 2)
	2
	"""
	return a if a > b else b

def absolute(a):
	"""
	Returns absolute value of a

	>>> absolute(4)
	4
	>>> absolute(-4)
	4
	"""
	return a if a >= 0 else a*-1


