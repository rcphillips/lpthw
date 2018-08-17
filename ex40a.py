import mystuff


class MyStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between"
		# init is the method that initiates the objects. 
		# it initiates the self object, and then gives that self object
		# a variable, or a key. in this case tangerine = some lyrics

	def apple(self):
		print("I AM CLASSY APPLES!!")


# You can use classes to craft many instances of MyStuff, and EACH ONE
# WON'T INTERFERE with the others.... so they can all have their own
# tangerine definitions? We can change them, etc?

# When you import a module, there is only one for the entire program.

# when you "instantiate" a class (create a class), what you get is called
# an object

thing = MyStuff()  # just instantiated a MyStuff object named thing
thing.apple()
print(thing.tangerine)

# to reiterate:
# dict style:
mystuff_dict = {'apples': 'I AM APPLES FROM A DICTIONARY!'}
print(mystuff_dict['apples'])

# module style:
# (see import at top)
mystuff.apple()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)