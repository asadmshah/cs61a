"""
CS61A Homework 4
"""

# Question 1

def reverse_list(s):
	"""
	Reverse the contents of list s and return None.

	>>> digits = [6, 2, 9, 5, 1, 4, 1, 3]
	>>> reverse_list(digits)
	>>> digits
	[3, 1, 4, 1, 5, 9, 2, 6]
	>>> d = digits
	>>> reverse_list(d)
	>>> digits
	[6, 2, 9, 5, 1, 4, 1, 3]
	"""
	for x in range(len(s) // 2):
		y = (x * -1) - 1
		s[x], s[y] = s[y], s[x]


# Question 2
def make_accumulator():
	"""
	Return an accumulator function that takesa  single numeric argument and
	accumulates that argument into total, then returns total.

	>>> acc = make_accumulator()
	>>> acc(15)
	15
	>>> acc(10)
	25
	>>> acc2 = make_accumulator()
	>>> acc2(7)
	7
	>>> acc3 = acc2
	>>> acc3(6)
	13
	>>> acc2(5)
	18
	>>> acc(4)
	29
	"""
	current = [0]
	def accumulator(x):
		current[0] += x
		return current[0]
	return accumulator


# Question 3
def make_accumulator_nonlocal():
	"""
	Return an accumulator function that takes a single numeric argument and
	accumulates that argument into total, then returns total.

	>>> acc = make_accumulator()
	>>> acc(15)
	15
	>>> acc(10)
	25
	>>> acc2 = make_accumulator()
	>>> acc2(7)
	7
	>>> acc3 = acc2
	>>> acc3(6)
	13
	>>> acc2(5)
	18
	>>> acc(4)
	29
	"""
	amount = 0
	def accumulator(x):
		nonlocal amount
		amount += x
		return amount
	return accumulator


# Question 4
def make_counter():
	"""
	Return a counter function.

	>>> c = make_counter()
	>>> c('a', 3)
	3
	>>> c('a', 5)
	8
	>>> c('b', 7)
	7
	>>> c('a', 9)
	17
	>>> c2 = make_counter()
	>>> c2(1, 2)
	2
	>>> c2(3, 4)
	4
	>>> c2(3, c('b', 6))
	17
	"""
	counts = {}
	def counter(k, v):
		counts[k] = counts.get(k, 0) + v
		return counts[k]
	return counter


# Question 5
from functools import reduce

def square(x):
	return x * x

def compose1(f, g):
	""" Return a function of that computes f(g(x)). """
	return lambda x: f(g(x))

def repeated(f, n):
	"""
	Return the function that computes the nth application of f, for n >= 1.

	f -- a function that takes one argument.
	n -- a positive integer.

	>>> repeated(square, 2)(5)
	625
	>>> repeated(square, 4)(5)
	152587890625
	"""
	assert type(n) == int and n > 0, "Bad n."
	return reduce(compose1, [f for x in range(n)])


# Question 6
def card(n):
	""" Return the playing card type for a positive n <= 13. """
	assert type(n) == int and n > 0 and n <= 13, "Bad card n."
	specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
	return specials.get(n, str(n))

def shuffle(cards):
	"""
	Return a shuffled list that interleaves the two halves of cards.

	>>> suits = ['♡', '♢', '♤', '♧']
	>>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
	>>> cards[:12]
	['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
	>>> cards[26:30]
	['7♤', '7♧', '8♡', '8♢']
	>>> shuffle(cards)[:12]
	['A♡', '7♤', 'A♢', '7♧', 'A♤', '8♡', 'A♧', '8♢', '2♡', '8♤', '2♢', '8♧']
	>>> shuffle(shuffle(cards))[:12]
	['A♡', '4♢', '7♤', '10♧', 'A♢', '4♤', '7♧', 'J♡', 'A♤', '4♧', '8♡', 'J♢']
	>>> cards[:12]  # Should not be changed
	['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
	>>> repeated(shuffle, 8)(cards) == cards
	True
	"""
	assert len(cards) % 2 == 0, 'len(cards) must be even.'
	h = len(cards) // 2
	h1, h2, shuffled = cards[:h], cards[h:], []
	for x in zip(h1, h2):
		shuffled += list(x)
	return shuffled


