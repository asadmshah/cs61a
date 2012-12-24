"""
CS61A Lab 3
Asad Shah
"""

from math import sqrt

# Exercise 2

def make_derivative(f, h=1e-5):
	"""
	Returns a function that is the derivative of f.

	>>> square = lambda x: x*x
	>>> derivative = make_derivative(square)
	>>> result = derivative(3)
	>>> round(result, 3)
	6.0
	"""
	def derivative(a):
		return (f(a + h) - f(a)) / h
	return derivative


# Exercise 3

def find_root(a, b, c):
	"""
	Returns one of two roots of a quadratic function.

	Since there are two roots to quadratics, return the larger root.
	In other words, the + or - part of the quadratic equation shoul
	just be replaced with a +

	>>> find_root(1, 2, 1)
	-1.0
	>>> find_root(1, -7, 12)
	4.0
	"""
	numerator = (-1 * b) + sqrt(discriminant(a, b, c))
	return numerator / 2 * a


def discriminant(a, b, c):
	"""
	Helper function for find_root that finds the discriminant of a, b, c.

	>>> discriminant(1, 2, 1)
	0
	>>> discriminant(1, -7, 12)
	1
	"""
	return pow(b, 2) - (4 * a * c)


# Exercise 4

def is_number(thing):
	"""
	Checks to see whether thing is a number.

	>>> is_number(4)
	True
	>>> is_number("Hello")
	False
	"""
	try:
		int(thing)
	except:
		return False
	return True

def type_check(func, pred, x):
	"""
	Checks to see whether the type of x is an accepted data type.
	If it is the result of the function with args x will be returned.
	Otherwise it'll just return false.

	>>> type_check(sqrt, is_number, "hello")
	False
	>>> type_check(sqrt, is_number, 4)
	2.0
	"""
	if pred(x):
		return func(x)
	return False

def make_safe(func, pred):
	"""
	Given a function and a checker, this function will return a new
	function that checks whether a given variable satisfies type
	requirements.

	>>> make_safe(sqrt, is_number)(4)
	2.0
	>>> make_safe(sqrt, is_number)("hello")
	False
	"""
	def safe_func(x):
		return type_check(func, pred, x)
	return safe_func


# Exercise 5

def cycle(f1, f2, f3):
	"""
	Returns a function that is itself a higher order function.

	>>> add1 = lambda x: x+1
	>>> mul2 = lambda x: x*2
	>>> add3 = lambda x: x+3
	>>> my_cycle = cycle(add1, mul2, add3)
	>>> identity = my_cycle(0)
	>>> identity(5)
	5
	>>> add_one_then_double = my_cycle(2)
	>>> add_one_then_double(1)
	4
	>>> do_all_functions = my_cycle(3)
	>>> do_all_functions(2)
	9
	>>> do_more_than_a_cycle = my_cycle(4)
	>>> do_more_than_a_cycle(2)
	10
	>>> do_two_cycles = my_cycle(6)
	>>> do_two_cycles(1)
	19
	"""
	def funcn(n):
		def funcx(x):
			i, s = 0, 1
			while i < n:
				if s == 1:
					x = f1(x)
					s += 1
				elif s == 2:
					x = f2(x)
					s += 1
				elif s == 3:
					x = f3(x)
					s = 1
				i += 1
			return x
		return funcx
	return funcn


