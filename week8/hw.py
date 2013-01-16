"""
CS61A Homework 7
"""

from operator import sub, mul

class Square(object):
	def __init__(self, side):
		self.side = side

class Rect(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height

def type_tag(s):
	return type_tag.tags[type(s)]

type_tag.tags = {Square: 's', Rect: 'r'}


def apply(operator_name, shape):
	"""
	Apply operator to shape.

	>>> apply("area", Square(10))
	100
	>>> apply("perimeter", Square(5))
	20
	>>> apply("area", Rect(5, 10))
	50
	>>> apply("perimeter", Rect(2, 4))
	12
	"""
	def sqa():
		return shape.side ** 2
	def sqp():
		return shape.side * 4
	def rea():
		return (shape.width * shape.height)
	def rep():
		return (shape.width * 2) + (shape.height * 2)
	funcs = {"s": {"area": sqa, "perimeter": sqp}, "r": {"area": rea, "perimeter": rep}}
	return funcs[type_tag(shape)][operator_name]()

def g(n):
	"""
	Return the value of G(n), computed recursively.

	>>> g(1)
	1
	>>> g(2)
	2
	>>> g(3)
	3
	>>> g(4)
	10
	>>> g(5)
	22
	"""
	if n <= 3:
		return n
	return g(n - 1) + 2 * g(n-2) + 3 * g(n-3)

def g_iter(n):
	"""
	Return the value of G(n), computed iteratively.

	>>> g_iter(1)
	1
	>>> g_iter(2)
	2
	>>> g_iter(3)
	3
	>>> g_iter(4)
	10
	>>> g_iter(5)
	22
	"""
	pass

def part(n):
	"""
	Return the number of partitions of positive integer n.

	>>> part(5)
	7
	>>> part(10)
	42
	>>> part(15)
	176
	>>> part(20)
	627
	"""
	pass

def make_anonymous_factorial():
	"""
	Return the value of an expression that computes factorial.

	>>> make_anonymous_factorial()(5)
	120
	"""
	total = [1]
	def factorial(x):
		if x <= 1:
			return total[0]
		total[0] *= x
		return factorial(x - 1)
	return factorial

