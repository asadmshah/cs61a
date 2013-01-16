"""
Discussion CS61A
"""

class Skittle(object):
	""" A skittle object has a color to describe it. """
	def __init__(self, color):
		self.color = color

class Bag(object):
	"""
	A bag is a collection of skittles. All bags share the number
	of bags ever made (sold) and each bag keeps track of its skittles
	in a list.
	"""
	number_sold = 0

	def __init__(self):
		self.skittles = ()
		Bag.number_sold += 1

	def tag_line(self):
		""" Print the skittles tag line. """
		print("Taste the rainbow")

	def print_bag(self):
		print(tuple(s.color for s in self.skittles))

	def take_skittle(self):
		"""
		Take the first skittle in the bag (from the front of the list.
		"""
		skittle_to_eat = self.skittles[0]
		self.skittles = self.skittles[1:]
		return skittle_to_eat

	def add_skittle(self, s):
		""" Add a skitle to the bag. """
		self.skittles += (s, )

	def take_color(self, color):
		for key in range(len(self.skittles)):
			if self.skittles[key].color == color:
				result = self.skittles[key]
				self.skittles = self.skittles[:key] + self.skittles[key + 1:]
				return result
		return None

	def take_all(self):
		for skittle in self.skittles:
			print skittle.color
		self.skittles = ()


class Email(object):
	"""
	Every email object has 3 instance attriutes: the message, the sender,
	and the addressee.
	"""
	def __init__(self, msg, sender, addressee):
		self.msg = msg
		self.sender = sender
		self.addressee = addressee


class Postman(object):
	"""
	Each postman has an instance attribute clients, which is a dictionary
	that associates client names with client objects.
	"""
	def __init__(self):
		self.clients = {}

	def send(self, email):
		"""
		Take an email and put it in the inbox of the client it is addressed to.
		"""
		self.clients[email.addressee].receive(email)

	def register_client(self, client, client_name):
		"""
		Takes a client object and client_name and adds it to the clients
		instance attribute.
		"""
		self.clients[client_name] = client


class Client(object):
	"""
	Every client has instance attributes name (which is used for addressing
	emails to the client), mailman (which is used to send emails out to other
	clients), and inbox (a tuple of all emails the clint has received).
	"""
	def __init__(self, mailman, name):
		self.inbox = ()
		self.name = name
		self.mailman = mailman

	def compose(self, message, recipient):
		"""
		Send an email with the given message msg to the given recipient.
		"""
		self.mailman.send(Email(message, self.name, recipient))
		

	def receive(self, email):
		"""
		Take an email and add it to the inbox of this client.
		"""
		self.inbox += (email, )


class Animal(object):
	def __init__(self):
		self.is_alive = True

class Pet(Animal):
	def __init__(self, name, dob, owner=None):
		Animal.__init__(self)
		self.name = name
		self.age = 2012 - dob
		self.owner = owner

	def eat(self, thing):
		print(self.name + " ate a " + str(thing) + "!")

	def talk(self):
		print("...")

class Dog(Pet):
	def __init__(self, name, yob, owner, color):
		Pet.__init__(self, name, yob, owner)
		self.color = color
	
	def talk(self):
		print("Woof!")

class Cat(Pet):
	def __init__(self, name, yob, owner, lives=9):
		Pet.__init__(self, name, yob, owner)
		self.lives = lives

	def talk(self):
		print("Meow!")
	
	def lose_life(self):
		self.lives -= 1

class NoisyCat(Cat):
	def __init__(self, name, yob, owner, lives=9):
		Cat.__init__(self, name, yob, owner, lives)
	
	def talk(self):
		Cat.talk()
		Cat.talk()

	
