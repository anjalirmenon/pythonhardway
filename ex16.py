from sys import argv
script, filename = argv

print "we are going to erase %r." % filename
print "if you dont want that, hit ctrl- c (^C)."
print "if u dont want that, hit ENTER."
raw_input("!")
print "opening the file.."
target = open(filename,'w')
print "truncate the file!!!"
target.truncate()
print "now type 2 lines."
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")

print "i'm going to write these to file."
target.write(line1)
target.write("\t \n")
target.write(line2)
target.write("\n")

print "and that is the file"
target.close()
