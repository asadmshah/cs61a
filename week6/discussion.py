"""
CS61A Discussion
Mutable List and Dictionaries
"""

def map_mut(function, lst):
	"""
	Maps function onto lst by mutation.

	>>> lst = [1, 2, 3, 4]
	>>> map_mut(lambda x: x**2, lst)
	>>> lst
	[1, 4, 9, 16]
	"""
	for i in range(len(lst)):
		lst[i] = function(lst[i])

def shift_left(lst, n):
	"""
	Shifts the elements of lst over by n indices.

	>>> lst = [1, 2, 3, 4, 5]
	>>> shift_left(lst, 2)
	>>> lst
	[3, 4, 5, 1, 2]
	"""
	i = 0
	while n < len(lst):
		lst.insert(i, lst.pop(n))
		n, i = n + 1, i + 1

def filter_mut(lst, pred):
	"""
	Filters lst by mutating it.

	>>> lst = [1, 2, 3, 4]
	>>> filter_mut(lst, lambda x: x % 2 == 0)
	>>> lst
	[2, 4]
	"""
	i = 0
	while i < len(lst):
		if pred(lst[i]):
			i += 1
		else:
			lst.pop(i)


def make_inverse_dict(d):
	"""
	Swap keys and values in given dictionary.

	>>> make_inverse_dict({"a": 1, "b": 2, "c": 3})
	{1: 'a', 2: 'b', 3: 'c'}
	"""
	return dict(zip(d.values(), d.keys()))
