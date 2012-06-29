# exercise 31

print "you are going to enter a zoo or a museum? for zoo press 1, for museum press 2"
ans = raw_input("--> ")

if ans == "1":
	print "you chose zoo, a tiger is on the loose! what are you going to do?"
	print "1) go find the tiger before tiger finds you"
	print "2) run for your life!"
	zoo = raw_input("--> ")
	if zoo == "1":
		print "haha! you are dead"
	elif zoo == "2":
		print "good thinking run.. run.. run.."
	else:
		print "ok that would be great!"

elif ans == "2":
	print " you chose museum, there is egyptian mummy's spirit missing.what are you planning "
	print "1) find the spirit!"
	print "2) better go back home"
	museum = raw_input("--> ")
	if museum == "1":
		print "no way! have you not heard about the curse!"
	elif museum == "2":
		print "now thats a nice move!"
	else:
		print "ok that would be great!"
else:
	print "today is good day to stay home and do %r!" % ans
