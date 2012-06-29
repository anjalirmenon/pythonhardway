from sys import argv
script, filename = argv

text = open(filename,'r')
print "here is your file %r:" % filename
print text.read()
print "type the filename again:"
filen = raw_input("->")
textn = open(filen,'r')
print textn.read()
