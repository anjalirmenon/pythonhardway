from sys import argv

script, input_file = argv

def printall(f):
  print f.read()

def rewind(f):
  f.seek(0)

def printaline(line_count, f):
  print line_count, f.readline()
current_file = open(input_file)
printall(current_file)
rewind(current_file)
print "lets print 2 lines:"
current_line = 1
printaline(current_line, current_file)
current_line = current_line + 1
printaline(current_line, current_file)

