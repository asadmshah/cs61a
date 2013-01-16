"""
Custom OOP Module.
"""

def make_instance(cls):
	"""
	Return a new object instance.
	"""
	def get_value(name):
		if name in attributes:
			return attributes[name]
		else:
			value = cls["get"](name)
			return bind_method(value, instance)
	def set_value(name, value):
		attributes[name] = value
	attributes = {}
	instance = {"get": get_value, "set": set_value}
	return instance

def bind_method(value, instance):
	""" Return a bound method if value is callable, or value otherwise """
	if callable(value):
		def method(*args):
			return value(instance, *args)
		return method
	return value

def make_class(attributes, base_class=None):
	""" Return a new class, which is a dispatch dictionary. """
	def get_value(name):
		if attributes.has_key(name):
			return attributes[name]
		elif base_class is not None:
			return base_class["get"](name)
	def set_value(name, value):
		attributes[name] = value
	def new(*args):
		return init_instance(cls, *args)
	cls = {"get": get_value, "set": set_value, "new": new}
	return cls

def init_instance(cls, *args):
	""" Return a new object with type cls, initialized with args. """
	instance = make_instance(cls)
	init = cls["get"]("__init__")
	if init:
		init(instance, *args)
	return instance


