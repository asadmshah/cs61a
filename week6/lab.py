"""
CS61A
Lab 6: Nonlocal assignment and shakespeare
"""

def make_fib():
	"""
	Returns a function that returns the next fibo number each time it is
	called.

	>>> fib = make_fib()
	>>> fib()
	1
	>>> fib()
	1
	>>> fib()
	2
	>>> fib()
	3
	"""
	x, y = 0, 1
	def fib():
		nonlocal x, y
		x, y = y, x + y
		return x
	return fib

def build_successors_table(tokens):
	"""
	Returns a dictionary where they keys are for each word's succesor(s) are
	the values.

	>>> text = "the cow eats the dog .".split(" ")
	>>> table = build_successors_table(text)
	>>> tst = {'the': ['cow', 'dog'], 'cow': ['eats'], 'eats': ['the'], 'dog': ['.'], '.': ['the']}
	>>> tst == table
	True
	"""
	table = {}
	prev = '.'
	for word in tokens:
		if prev in table:
			table[prev].append(word)
		else:
			table[prev] = [word]
		prev = word
	return table

def construct_sentence(word, table):
	import random
	result = ''
	while word not in ['.', '!', '?']:
		result += word + " "
		word = random.choice(table[word])
	return result + word

def shakespeare_tokens(path="shakespeare.txt", url="http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt"):
	""" Return the words of Shakespeare's plays as a list. """
	import os
	from urllib.request import urlopen
	if os.path.exists(path):
		result = open("shakespeare.txt", encoding="ascii").read().split()
	else:
		shakespeare = urlopen(url)
		result = shakespeare.read().decode(encoding="ascii").split()
	return result


