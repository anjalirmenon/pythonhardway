#exercise 42

class Animal(object):
	pass
class Dog(Animal):
	def __init__(self,name):
		self.name = name

class Person(object):
	def __init__(self, name):
		self.name = name
		self.pet = None
roger = Dog("roger")
annie = Person("annie")
louis = Person("louis")
louis.pet = roger
#print louis.pet
