"""
Week 8 Lab
"""

from oop import *

def make_person1(name, age):
	def person(message):
		if message == "name":
			return name
		elif message == "age":
			return age
		else:
			return "I don't understand that message."
	return person

def make_person2(name, age):
	inventory = []
	def dispatch(message, additional=None):
		if message == "name":
			return name
		elif message == "age":
			return age
		elif message == "buy" and additional:
			inventory.append(additional)
			return "I just bought a", additional
		elif message == "change name" and additional:
			#nonlocal name
			name = additional
		elif message == "inventory":
			return inventory
		else:
			return "I don't understand that message."
	return dispatch

def make_person3(name, age):
	attributes = {"name": name, "age": age, "inventory": []}
	def get_name():
		return attributes["name"]
	def get_age():
		return attributes["age"]
	def get_inventory():
		return attributes["inventory"]
	def buy(item):
		attributes.append(item)
	def change_name(to):
		attributes["name"] = to
	person = {"name": get_name, "age": get_age, "inventory": get_inventory,
			"buy": buy, "change_name": change_name}
	return person


# Question 4

def make_vending_machine_class():
	def __init__(self, name, price):
		self["set"]("name", name)
		self["set"]("price", price)
		self["set"]("stock", 0)
		self["set"]("balance", 0)
		return self

	def vend(self):
		if self["get"]("stock") <= 0:
			return "Machine is out of stock."
		change = self["get"]("balance") - self["get"]("price")
		if change < 0:
			required = self["get"]("price") - self["get"]("balance")
			return "You must deposit $%s" % required
		self["set"]("stock", self["get"]("stock") - 1)
		self["set"]("balance", 0)
		result = "Here is your " + self["get"]("name")
		if change:
			result += " and $" + str(change) + " change"
		return result + "."

	def restock(self, amount):
		result = self["get"]("stock") + amount
		self["set"]("stock", result)
		return "Current crab stock: {0}".format(result)

	def deposit(self, amount):
		result = self["get"]("balance") + amount
		if self["get"]("stock") < 1:
			return "Machine is out of stock. Here is your $%d" % result
		self["set"]("balance", result)
		return "Current balance: $%d" % result

	return make_class({"__init__": __init__, "vend": vend, "restock": restock,
						"deposit": deposit})
		
