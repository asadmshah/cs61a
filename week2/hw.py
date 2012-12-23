"""
CS61A Homework 2
Asad Shah
"""

from operator import add
from operator import mul

def square(x):
	"""
	Return square of x.

	>>> square(4)
	16
	"""
	return x * x

# Question 1

def summation(n, term):
	"""
	Return the sum of the first n terms in a sequence.

	>>> summation(4, square)
	30
	"""
	t, i = 0, 1
	while i <= n:
		t += term(i)
		i += 1
	return t

def product(n, term):
	"""
	Return the product of the first n terms in a sequence.

	>>> product(4, square)
	576
	"""
	t, i = 1, 1
	while i <= n:
		t *= term(i)
		i+=1
	return t

def factorial(n):
	"""
	Return n factorial by calling product.

	>>> factorial(4)
	24
	"""
	if n <= 1:
		return n
	return n * factorial(n-1)

# Question 2

def accumulate(combiner, start, n, term):
	"""
	Return the result of combining the first n terms in a sequence.
	"""
	t, i = start, 1
	while i <= n:
		t = combiner(t, term(i))
		i += 1
	return t


def summation_using_accumulate(n, term):
	"""
	An implementation of summation using accumulate.

	>>> summation_using_accumulate(4, square)
	30
	"""
	return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
	"""
	An implementation of product using accumulate.

	>>> product_using_accumulate(4, square)
	576
	"""
	return accumulate(mul, 1, n, term)

# Question 3

def double(function):
	"""
	Return a function that applies f twice.

	>>> double(square)(2)
	16
	"""
	def functioner(x):
		return function(function(x))
	return functioner


# Question 4

def repeated(f, n):
	"""
	Return the function that computes the nth application of f.

	>>> repeated(square, 2)(5)
	625
	>>> repeated(square, 4)(5)
	152587890625
	"""
	f = double(f)
	while n > 3:
		f = double(f)
		n -= 1
	return f

# Question 5


