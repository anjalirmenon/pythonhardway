#exercise 18

def print_two(*ar):
  arg1, arg2 = ar
  print "arg1: %r, args: %r" % (arg1, arg2)
def print_again(arg1, arg2):
  print "arg1: %r, arg2: %r" % (arg1, arg2)
def print_first(arg1):
  print "arg1: %r" % arg1


def print_0():
  print "i got nothing to parse"

print_two("anjali","menon")
print_again("anjali","menon")
print_first("anjali")
print_0()
