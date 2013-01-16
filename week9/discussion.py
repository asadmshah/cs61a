"""
CS61A Discussion
"""

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


def sum_primes_up_to(n):

