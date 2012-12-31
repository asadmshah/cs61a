"""
CS61A
Discussion 3
Newton's Method and Sequences
"""

## Tuples

# Question 1
def sum(tup):
	"""
	Sums up the tuple.

	>>> sum((1, 2, 3, 4, 5))
	15
	"""
	total, i = 0, 0
	while i < len(tup):
		total += tup[i]
		i += 1
	return total

# Question 2
def min_element(tup):
	"""
	Returns the minimum element in tup.

	>>> min_element((1, 2, 3, 2, 1))
	1
	"""
	lowest, i = tup[0], 0
	while i < len(tup):
		if i < lowest:
			lowest = tup[i]
		i += 1
	return lowest

# Question 3
def map_tuple(func, tup):
	"""
	Applies func to each element of tup and returns a new tuple.

	>>> map_tuple(lambda x: x*x, (1, 2, 3, 4))
	(1, 4, 9, 16)
	"""
	new, i = (), 0
	while i < len(tup):
		new += (func(tup[i])),
		i += 1
	return new

# Question 4
def cartesian_product(tuple1, tuple2):
	"""
	Returns a tuple that is the cartesian product of tuple1 and tuple2.

	>>> cartesian_product((1,2), (4,5))
	((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))
	"""
	result, x = (), 0
	while x < len(tuple1):
		y = 0
		while y < len(tuple2):
			temp1 = (tuple1[x], tuple2[y])
			temp2 = (tuple2[y], tuple1[x])
			result += (temp1, temp2)
			y += 1
		x += 1
	return result

## Sequence Iteration with For Loops

# Question 1
def sum(sequence):
	"""
	Returns the sum of all elements in sequence.

	>>> sum([1, 2, 3, 4, 5])
	15
	"""
	total = 0
	for i in sequence:
		total += i
	return total

# Question 2
def filter(pred, sequence):
	"""
	Returns a new list with elements from original list that pass pred.

	>>> filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
	[2, 4]
	"""
	result = []
	for item in sequence:
		if pred(item):
			result.append(item)
	return result

def cartesian_product_for(seq1, seq2):
	"""
	cartesian_product utilizing a for loop.

	>>> cartesian_product_for( (1, 2), (3, 4) )
	((1, 3), (3, 1), (1, 4), (4, 1), (2, 3), (3, 2), (2, 4), (4, 2))
	"""
	result = ()
	for x in seq1:
		for y in seq2:
			result += ( (x, y), (y, x) )
	return result


## Data Abstraction

def make_point(x, y):
	return (x, y)

def get_x(point):
	return point[0]

def get_y(point):
	return point[1]

def make_segment(pt1, pt2):
	return (pt1, pt2)

def start_pt(seg):
	return seg[0]

def end_pt(seg):
	return seg[1]

def reflect_across_y(seg):
	"""
	Returns a line segments that is the y-axis reflection of segment.

	>>> reflect_across_y(make_segment(make_point(0, 0), make_point(4, 5)))
	((0, 0), (-4, 5))
	"""
	x, y = end_pt(seg)
	new_pt = make_point(x * -1, y)
	return make_segment(start_pt(seg), new_pt)

def midpoint(segment):
	pt1 = start_pt(seg)
	pt2 = end_pt(seg)
	new_x = (get_x(pt1), get_x(pt2)) // 2
	new_y = (get_y(pt1), get_y(pt2)) // 2
	return make_point(new_x, new_y)
