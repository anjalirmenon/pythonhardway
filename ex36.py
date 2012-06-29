# exercise 36 game code
# finding the princess
def door():
	print "you are inside the castle choose door: 1, 2 , 3"
	doorno = raw_input("> ")
	if doorno == "1":
		print"enter house of swords!"
		sword_room()
	elif doorno == "2":
		print "enter dragon waiting!!!"
		dragon()
	elif doorno == "3":
		print "this is door to exit you can carry on without the princess!"
		exit(0)
	else:
		print "there are no doors for you"
		exit(0)
def sword_room():
	print "if you move inside the swords will chop-chop"
	print "what do u plan to do?1. jump around 2. deactivate- the swords"
	sword = raw_input("> ")
	if sword == "jump around":
		print "you are beheaded.game over for you."
		task()
	elif sword == "deactivate":
		print "smart move! choose new doors to go further"
		print "1. left 2. right"
		door2 = raw_input("> ")
		if door2 == "left":
			dragon()
		elif door2 == "right":
			print "you dont fight the dragon."
			find_princess()
		else:
			print "there is no such door!"
			exit(0)
def dragon():
	print "the dragon is angry and waiting to burn you down"
	print "Quick! make a choice 1. fight 2. behead dragon"
	drag = raw_input("> ")
	if drag == "fight":
		print "you cant fight a dragon silly!"
		exit(0)
	elif drag == "behead":
		print "wise guy! move ahead and find princess in the next room."
		find_princess()
	else:
		print "i dont understand!"
		exit(0)
def find_princess():
	print "hurray! you saved the princess. take her away and rule her kingdom!"
	exit(0)
			

def task():
	print """
		you are going to enter the castle where the princess is captured! she is guarded by a fiery dragon. to reach her you have to kill the dragon. beware of your choices some where is room of swords waiting to chop
"""
print "do u wish to enter the castle type y/n?:"
enter = raw_input("> ")
if enter == 'n':
	print "you are a coward!"
	exit(0)
elif enter == 'y':
	print "brave fellow!"
	door()
else:
	print "you think its funny to type wrong entry?"
	exit(0)

task()
