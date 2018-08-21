'''
Most of the uses of inheritance can be simplified or replaced with 
composition. Multiple inheritance should be avoided at all costs.
'''

# Implicit Inheritance
# in which you define a function in the parent, but not the child.


class Parent(object):
	# "base class"
	def implicit(self):
		print("PARENT implicit()")


class Child(Parent):
	# "sub class"
	pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()