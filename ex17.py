#exercise 17

from sys import argv
from os.path import exists

script, fromfile, tofile = argv
print "printing from %r to %r" % (fromfile, tofile)

input = open(fromfile, 'r')
inputdata = input.read()
print "does the tofile exists? %r" % exists(tofile)
print "hit enter to continue or ctrl c to quit"
raw_input()

output = open(tofile, 'w')
output.write(inputdata)
print "copy over"
output.close()
input.close()
