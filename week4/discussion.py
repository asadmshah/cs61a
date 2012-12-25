"""
CS61A Week 4
Discussion 2: Higher Order Functions.
"""

from math import sqrt

################################################################################
# Warmup Questions

def slow_is_prime(n):
	k = 2
	while k < n:
		if n % k == 0:
			return False
		k += 1
	return True

def average_is_prime(n):
	k = 2
	while k < sqrt(n) + 1:
		if n % k == 0:
			return False
		k += 1
	return True

def faster_is_prime(n):
	if n % 2 == 0:
		return False
	k = 3
	while k < sqrt(n) + 1:
		if n % k == 0:
			return False
		k += 2
	return True

def nth_prime(n):
	prime, count, check = 0, 1, 2
	while count < n:
		if faster_is_prime(check):
			prime = check
			count += 1
		check += 1
	return prime

def nth_fibo(n):
	prev, after, count = 0, 1, 2
	while count < n:
		prev, after, count = after, prev + after, count + 1
	return after


################################################################################
# Procedures as Argument Values

def square(x):
	return x * x

def double(x):
	return x + x

def old_square_every_number(n):
	k = 1
	while k <= n:
		print(square(k))
		k += 1

def old_double_every_number(n):
	k = 1
	while k <= n:
		print(double(k))
		k += 1

def square_every_number(n):
	every(n, square)

def double_every_number(n):
	every(n, double)

def every(func, n):
	k = 1
	while k <= n:
		print(func(k))
		k += 1

def keep(cond, n):
	k = 1
	while k <= n:
		if cond(k):
			print(k)
		k += 1


################################################################################
# Procedures as Return Values

def and_add_one(f):
	def adder_function(x):
		return f(x) + 1
	return adder_function

def and_add(f, n):
	def adder_function(x):
		return f(x) + n
	return adder_function

