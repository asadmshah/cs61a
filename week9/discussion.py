"""
CS61A Discussion
"""

from math import sqrt

def countdown(n):
	"""
	>>> countdown(5)
	5
	4
	3
	2
	1
	"""
	if n <= 0:
		return
	print(n)
	countdown(n-1)


def countup(n):
	"""
	>>> countup(5)
	1
	2
	3
	4
	5
	"""
	if n <= 0:
		return
	countup(n-1)
	print(n)


def expt(base, power):
	"""
	>>> expt(3, 2)
	9
	>>> expt(2, 3)
	8
	"""
	if power <= 0:
		return 1
	return base * expt(base, power - 1)


def map(function, sequence):
	"""
	>>> map(lambda x: x*x, [1, 2, 3, 4])
	[1, 4, 9, 16]
	"""
	if sequence == []:
		return sequence
	return [function(sequence[0])] + map(function, sequence[1:])


def merge(list1, list2):
	"""
	>>> merge([1, 2, 5, 7, 10, 11], [3, 6, 12])
	[1, 2, 3, 5, 6, 7, 10, 11, 12]
	"""
	if list1 == []:
		return list2
	elif list2 == []:
		return list1
	else:
		if list1[0] < list2[0]:
			return [list1[0]] + merge(list1[1:], list2)
		else:
			return [list2[0]] + merge(list1, list2[1:])


def is_prime(x):
	"""
	>>> is_prime(2)
	True
	>>> is_prime(3)
	True
	>>> is_prime(4)
	False
	>>> is_prime(12)
	False
	>>> is_prime(19)
	True
	"""
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	p = 3
	while p < sqrt(x) + 1:
		if x % p == 0:
			return False
		p += 2
	return True


def sum_primes_up_to(n):
	"""
	>>> sum_primes_up_to(5)
	10
	>>> sum_primes_up_to(10)
	17
	"""
	if n <= 1:
		return 0
	elif is_prime(n):
		return n + sum_primes_up_to(n - 1)
	else:
		return 0 + sum_primes_up_to(n - 1)


def sum_filter_up_to(n, pred):
	"""
	>>> sum_filter_up_to(5, is_prime)
	10
	>>> sum_filter_up_to(10, is_prime)
	17
	"""
	if n <= 1:
		return 0
	elif pred(n):
		return n + sum_filter_up_to(n - 1, pred)
	else:
		return 0 + sum_filter_up_to(n - 1, pred)


def count_stair_ways(n):
	if n <= 1:
		return 1
	if n == 2:
		return 2
	else:
		return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def pascal(row, column):
	if row == column or column == 0:
		return 1
	else:
		return pascal(row - 1, column) + pascal(row - 1, column - 1)

def has_sum(target, n1, n2):
	"""
	>>> has_sum(1, 3, 5)
	False
	>>> has_sum(5, 3, 5)
	True
	>>> has_sum(11, 3, 5)
	True
	"""
	if n1 + 0 == target:
		return True
	elif n2 + 0 == target:
		return True
	elif n1 + n2 > target:
		return False
	elif n1 + n2 == target:
		return True
	else:
		return has_sum(target, n1 + n1, n2) or has_sum(target, n1, n2 + n2)

def subset_sum(sequence, target):
	"""
	>>> subset_sum([2, 4, 7, 3], 5)
	True
	>>> subset_sum([1, 9, 5, 7, 3], 2)
	False
	>>> subset_sum([1, 1, 5, -1], 3)
	False
	"""
	pass


def mergesort(sequence):
	"""
	>>> mergesort([1, 5, 2, 4, 3])
	[1, 2, 3, 4, 5]
	>>> mergesort([1, 9, 2, 3, 4, 8, 7, 5, 6])
	[1, 2, 3, 4, 5, 6, 7, 8, 9]
	"""
	if len(sequence) <= 1:
		return sequence
	else:
		mid = len(sequence) // 2
		left = mergesort(sequence[:mid])
		right = mergesort(sequence[mid:])
		return merge(left, right)

