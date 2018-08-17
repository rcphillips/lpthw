# It's important to distinguish whether something is a class.
# or an object.

# objects are specific entities in code. An object is an example of a class.
# A class can also be an example of another class. is-a. inheritance.

# Animal is-a object


class Animal(object):
	pass

# Dog is-a Animal


class Dog(Animal):

	def __init__(self, name):
		self.name = name


# Cat is-a Animal


class Cat(Animal):

	def __init__(self, name):
		# class Cat has-a init that takes self and name as params.
		self.name = name

# class Person is-a object


class Person(object):

	def __init__(self,name):
		self.name = name
		# class Person has-a init that takes self and name as params.
		self.pet = None

# class Employee is-a Person


class Employee(Person):

	def __init__(self, name, salary):
		super(Employee, self).__init__(name)  # something about parent classes?
		# class Employee has-a attribute that takes salary as its param?
		self.salary = salary

# class Fish is-a object


class Fish(object):
	pass


class Salmon(Fish):
	pass


class Halibut(Fish):
	pass


rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

