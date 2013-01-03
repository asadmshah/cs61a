"""
CS61A
Homework 5
"""

# Question 1

def count_calls(f):
	"""
	A function that returns a version of that counts calls to f and can
	report that count to how_many_calls.

	>>> from operator import add
	>>> counted_add, add_count = count_calls(add)
	>>> add_count()
	0
	>>> counted_add(1, 2)
	3
	>>> add_count()
	1
	>>> add(3, 4)
	7
	>>> add_count()
	1
	>>> counted_add(5, 6)
	11
	>>> add_count()
	2
	"""
	count = 0
	def counter():
		nonlocal count
		return count
	def modded_func(*args):
		nonlocal count
		count += 1
		return f(*args)
	return modded_func, counter


def make_withdraw(balance, password):
	"""
	Return a password-protected withdraw function.

	>>> w = make_withdraw(100, "pass")
	>>> w(25, "pass")
	75
	>>> w(90, "pass")
	'Insufficient funds'
	>>> w(25, "hwat")
	'Incorrect password'
	>>> w(25, "pass")
	50
	>>> w(75, "a")
	'Incorrect password'
	>>> w(10, "pass")
	40
	>>> w(20, "n00b")
	'Incorrect password'
	>>> w(10, "pass")
	"Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
	>>> w(10, "l33t")
	"Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
	"""
	attempts = []
	def account(amount, the_pass):
		nonlocal balance
		if len(attempts) == 3:
			return "Your account is locked. Attempts: {0}".format(attempts)
		elif the_pass != password:
			attempts.append(the_pass)
			return "Incorrect password"
		elif amount > balance:
			return "Insufficient funds"
		else:
			balance -= amount
			return balance
	return account


# Question 3

def make_joint(joint_account, old_password, new_password):
	"""
	Return a password-protected withdraw function that has joint access to
	the balance of withdraw.

	>>> w = make_withdraw(100, "hax0r")
	>>> w(25, "hax0r")
	75
	>>> make_joint(w, "my", "secret")
	'Incorrect password'
	>>> j = make_joint(w, "hax0r", "secret")
	>>> w(25, "secret")
	'Incorrect password'
	>>> j(25, "secret")
	50
	>>> j(25, "hax0r")
	25
	>>> j(100, "secret")
	'Insufficient funds'
	>>> j2 = make_joint(j, "secret", "code")
	>>> j2(5, "code")
	20
	>>> j2(5, "secret")
	15
	>>> j2(5, "hax0r")
	10
	>>> j2(25, "password")
	'Incorrect password'
	>>> j2(5, "secret")
	"Your account is locked. Attempts: ['my', 'secret', 'password']"
	>>> j(5, "secret")
	"Your account is locked. Attempts: ['my', 'secret', 'password']"
	>>> w(5, "hax0r")
	"Your account is locked. Attempts: ['my', 'secret', 'password']"
	>>> make_joint(w, "hax0r", "hello")
	"Your account is locked. Attempts: ['my', 'secret', 'password']"
	"""
	init_verification = joint_account(0, old_password)
	if type(init_verification) not in [int, float]:
		return init_verification
	def account(amount, password):
		if password == new_password:
			password = old_password
		return joint_account(amount, password)
	return account


