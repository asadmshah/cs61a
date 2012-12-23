"""
CS61A Homework 1
Name: Asad Shah
"""

# Question 1

from operator import add, sub
def a_plus_abs_b(a, b):
	"""
	Return a+abs(b), but with out calling abs.
	
	>>> a_plus_abs_b(2, 3)
	5
	>>> a_plus_abs_b(2, -3)
	5
	"""
	if b < 0:
		op = sub
	else:
		op = add
	return op(a, b)


# Question 2

def two_of_three(a, b, c):
	"""
	Return x*x + y*y, where x and y are the two largest of a, b, c.

	>>> two_of_three(1, 2, 3)
	13
	>>> two_of_three(5, 3, 1)
	34
	>>> two_of_three(10, 2, 8)
	164
	>>> two_of_three(5, 5, 5)
	50
	"""
	return max(a,b,c)**2 + (a+b+c-min(a,b,c)-max(a,b,c))**2


# Question 4

def hailstone(n):
	"""
	Print the hailstone sequence starting at n and returns
	its length.

	>>> a = hailstone(10)
	10
	5
	16
	8
	4
	2
	1
	>>>
	7
	"""
	elements = []
	print(n)
	elements.append(n)
	while n > 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = (n * 3) + 1
		print(n)
		elements.append(n)
	return elements
