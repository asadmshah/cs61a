"""
CS61A Homework 6
"""

# Question 1

class VendingMachine(object):
	"""
	A vending machine that vends some product for some price.

	>>> v = VendingMachine('crab', 10)
	>>> v.vend()
	'Machine is out of stock.'
	>>> v.restock(2)
	'Current crab stock: 2'
	>>> v.vend()
	'You must deposit $10 more.'
	>>> v.deposit(7)
	'Current balance: $7'
	>>> v.vend()
	'You must deposit $3 more.'
	>>> v.deposit(5)
	'Current balance: $12'
	>>> v.vend()
	'Here is your crab and $2 change.'
	>>> v.deposit(10)
	'Current balance: $10'
	>>> v.vend()
	'Here is your crab.'
	>>> v.deposit(15)
	'Machine is out of stock. Here is your $15.'
	"""

	def __init__(self, product, price):
		self.product = product
		self.price = price
		self.stock = 0
		self.balance = 0

	def vend(self):
		if self.stock < 1:
			return "Machine is out of stock."
		elif self.balance < self.price:
			diff = self.price - self.balance
			return "You must deposit ${0} more.".format(diff)
		else:
			self.stock -= 1
			change = self.balance - self.price
			self.balance = 0
			if change > 0:
				return "Here is your {0} and ${1} change.".format(self.product, change)
			else:
				return "Here is your {0}.".format(self.product)

	def deposit(self, amount):
		if self.stock < 1:
			return "Machine is out of stock. Here is your ${0}.".format(amount)
		else:
			self.balance += amount
			return "Current balance: ${0}".format(self.balance)

	def restock(self, stock):
		self.stock += stock
		return "Current {0} stock: {1}".format(self.product, self.stock)


# Question 2

class MissManners(object):
	"""
	A container class that only forward messages that say please.

	>>> v = VendingMachine('teaspoon', 10)
	>>> v.restock(2)
	'Current teaspoon stock: 2'
	>>> m = MissManners(v)
	>>> m.ask('vend')
	'You must learn to say please.'
	>>> m.ask('please vend')
	'You must deposit $10 more.'
	>>> m.ask('please deposit', 20)
	'Current balance: $20'
	>>> m.ask('now will you vend?')
	'You must learn to say please.'
	>>> m.ask('please give up a teaspoon')
	'Thanks for asking, but I know not how to give up a teaspoon'
	>>> m.ask('please vend')
	'Here is your teaspoon and $10 change.'
	"""
	def __init__(self, vendor):
		self.vendor = vendor

	def ask(self, message, *args):
		if "please" in message:
			call = message[7:]
			if hasattr(self.vendor, call):
				return getattr(self.vendor, call)(*args)
			else:
				return "Thanks for asking, but I know not how to {0}".format(call)
		else:
			return "You must learn to say please."


# Question 3

class Amount(object):
	"""
	An amount of nickels and pennies.

	>>> a = Amount(3, 7)
	>>> a.nickels
	3
	>>> a.pennies
	7
	>>> a.value
	22
	>>> a.nickels = 5
	>>> a.value
	32
	"""
	def __init__(self, nickels, pennies):
		self.nickels = nickels
		self.pennies = pennies

	@property
	def value(self):
		return (self.nickels * 5) + self.pennies

class MinimalAmount(Amount):
	"""
	An amount of nickels and pennies that is initialized with no more than
	four pennies, by converting excess pennies to nickels.

	>>> a = MinimalAmount(3, 7)
	>>> a.nickels
	4
	>>> a.pennies
	2
	>>> a.value
	22
	"""
	def __init__(self, nickels, pennies):
		self.nickels = nickels + (pennies // 5)
		self.pennies = pennies % 5


# Question 4

class Container(object):
	"""
	A container for a single item.

	>>> c = Container(12)
	>>> c
	Container(12)
	>>> len(c)
	1
	>>> c[0]
	12
	"""
	def __init__(self, item):
		self._item = item

	def __repr__(self):
		return "Container({0})".format(repr(self._item))

	def __len__(self):
		return 1

	def __getitem__(self, index):
		assert index == 0, "A container holds only one item"
		return self._item

class Rlist(object):
	"""
	A recursive list consisting of a first element and the rest.

	>>> s = Rlist(1, Rlist(2, Rlist(3)))
	>>> len(s)
	3
	>>> s[0]
	1
	>>> s[1]
	2
	>>> s[2]
	3
	"""
	def __init__(self, *args):
		self._head = args[0]
		if len(args) > 1:
			self._tail = args[1]

	def __len__(self):
		lst, count = self, 1
		while hasattr(lst, "_tail"):
			lst = lst._tail
			count += 1
		return count

	def __getitem__(self, index):
		lst = self
		while index > 0:
			lst = lst._tail
			index -= 1
		return lst._head


