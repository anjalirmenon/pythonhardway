#exercise 45

#game mission escape to gullin's island
from sys import exit
from random import randint	

class Game(object):
	
	def __init__(self, begin):
		
		self.stmnt = ["common that was a stupid way to die!","Did it hurt? well its ok coz you are dead now!","you lose! play when you are ready next time!"]
		self.begin = begin
	def playon(self):
		newplace = self.begin
		while True:
			print "\n######"
			place = getattr(self, newplace)
			newplace = place()

	def dead(self):
		print self.stmnt[randint(0, len(self.stmnt)-1)]
		exit(0)
	def island(self):
		print "enter your name:"
		name = raw_input(" ")
		print "You are %s you are stuck in this dangerous island of Gullin." % name
		print "Your aim is to escape from the island, but there is a catch!You cant escape without a \'key\'. The key leads you to incibility potion. This is the only way to escape route. Go through trecherous ways and make right choices, coz Gullin's island no one has ever escaped!"
		print "\n"
		print "you are standing at the far end. you have to cross the moth inhabited by crocodiles and alligators."
		print " what do you plan to do? 1.swing across through the rope, 2.tickle the crocodiles, 3.stomp on the crocodiles heads and cross"
		choice = raw_input("> ")
		if choice == "1":
			print "the rope breaks in the middle and you land on the hungry crocodiles who relish you and you are dead."
			return 'dead'
		
		elif choice == "2":
			print "The crocodiles like you very much. they find you friendly and let you cross the moth easily."
			return 'swampy_moore'
		elif choice == "3":
			print "oh! oh! you shouldn't have. they are angry and tear their way through you"
			return 'dead'
		else:
			print "there are no means to do that"
			return 'island'
	def swampy_moore(self):
		print "swampy moore is too gluey for you to pass through easily. once you are able to cross it you can reach the cave of Alora to find the key to the potion."
		print "if u walk through the swamp it will swallow you. how will you pass through? 1.climb a tree and pass over, 2. use a long pole to vault over, 3. add a sack of cement"
		ch = raw_input("> ")
		if ch == "1":
			print "tree branch breaks. and you crash into the swamp.all you can remember is many bubbles."
			return 'dead'
		elif ch == "2":
			print "accidently you stick to the beginning of swamp, and vault inside the swamp and sink!"
			return 'dead'
		elif ch == "3":
			print "smart move! cement solidifies. now you can easily walk through"
			return 'alora_cave'
		else:
			print "now that is something you cant do!"
			return 'swampy_moore'
	def alora_cave(self):
		
		print "welcome! inside the cave. now you need to find the golden key that opens the door that hides the potion."
		print "you have to enter the correct 2 digit combination to open the stone lion's mouth.but beware you have only 5 chances to do so."
		print "if you enter a wrong code you hear a click sound and after final try the cave comes crashing down and crushes you to death."
		code = "%d%d" % (randint(1,9), randint(1,9))
		trials = 0
		print "enter the code:"
		trial = raw_input("> ")
		while trial != code and trials < 5:
			print "click!"
			trials = trials + 1
			trial = raw_input("> ")

		if trial == code:
			print "yes the lion's mouth opens and you can take away the key. move to the broken temple to try to find the door with your key."
			return 'temple'
		else:
			print "the cave strts to rumble and the stones and boulders come crashing sown crushing you to death."
			return 'dead'

	def temple(self):
		
		print "Now to the final. you have the key now there are the 3 doors and only 1 holds the potion for you to escape."
		print "behind one of the doors is the ghost of Gullin which will take your soul away. so make your choice well: 1 2 3"
		cho = raw_input(" ")
		if cho == "1":
			print "sorry the door doesnt have the potion, it was a poison u drank, oh u were so close to winning!"
			return 'dead'
		elif cho == "2":
			print "buhaaaa!!! I am the ghost of Gullin and your soul is mine!"
			return 'dead'
		elif cho == "3":
			print "yeahh!! you found the potion. you are the only living to escape from Gullin island."
			print "good play you win!"
			exit(0)
player = Game("island")
player.playon()
