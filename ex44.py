#exercise 44

class Parent(object):
	def implicit(self):
		print "Parent implicit()"
	def altered(self):
		print "Parent altered"
class Child(Parent):
#	pass
#	def implicit(self):
#		print "Child implicit()"
	def implicit(self):
		print "Child, before PARENT implicit()"
		super(Child, self).implicit()
		print "CHILD, after PARENT implicit()"
dad = Parent()
son = Child()

dad.implicit()
son.implicit()	
