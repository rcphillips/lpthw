# alter before or after.

# you can use super() to alter a parent? sound dangerous.


class Parent(object):

	def altered(self):
		print("PARENT altered")


class Child(Parent):

	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered()
		print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()


dad.altered()
son.altered()