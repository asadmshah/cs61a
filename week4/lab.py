"""
CS61A Lab 4: Data Abstraction
"""

# Exercise 4

def make_rat(num, den):
	return (num, den)

def num(rat):
	return rat[0]

def den(rat):
	return rat[1]

def mul_rat(a, b):
	nn = num(a) * num(b)
	nd = den(a) * den(b)
	return make_rat(nn, nd)

def str_rat(x):
	return "{0}/{1}".format(num(x), den(x))

def div_rat(a, b):
	nn = num(a) * den(b)
	nd = num(b) * den(a)
	return make_rat(nn, nd)


# Exercise 5

def make_segment(a, b):
	return (a, b)

def start_segment(seg):
	return seg[0]

def end_segment(seg):
	return seg[1]

def make_point(x, y):
	return (x, y)

def x_point(point):
	return point[0]

def y_point(point):
	return point[1]

def midpoint_segment(seg):
	start = start_segment(seg)
	end = end_segment(seg)
	mx = (x_point(start) + x_point(end)) / 2
	my = (y_point(start) + y_point(end)) / 2
	return make_point(mx, my)

# Exercise 6

def make_pair(x, y):
	def dispatch(m):
		if m == 0:
			return x
		elif m == 1:
			return y
		elif m == "pair":
			return (x, y)
		else:
			raise AssertionError("Message not recognized")
	return dispatch


# Exercise 7

def make_rectangle(length, width):
	return (length, width)

def rec_width(rectangle):
	return rectangle[1]

def rec_length(rectangle):
	return rectangle[0]

def perimeter(rectangle):
	l2 = rec_length(rectangle) * 2
	w2 = rec_width(rectangle) * 2
	return l2 + w2

def area(rectangle):
	return rec_width(rectangle) * rec_length(rectangle)
