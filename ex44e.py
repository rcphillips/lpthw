# composition is safer? than inheritance.


class Other(object):

	def override(self):
		print("OTher override()")

	def implicit(self):
		print("OTHER implicit()")

	def altered(self):
		print("OTHER altered()")


class Child(object):  # note how this is not inheritance at all

	def __init__(self):
		self.other = Other()  # but it does have an attribute that IS an
							  # other object.

	def implicit(self):
		self.other.implicit()

	def override(self):
		print("Child override()")

	def altered(self):
		print("CHILD BEFORE")
		self.other.altered()
		print("CHILD AFTER")


son = Child()

son.implicit()
son.override()
son.altered()