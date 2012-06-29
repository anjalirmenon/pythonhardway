# exercise 33

i = 0
number = []
while i < 6:
	print "at the top i is %d" % i
	number.append(i)
	i = i + 1
	print "number now: ", number
	print "at the bottom i is %d" % i

print "the numbers"
for num in number:
	print num
