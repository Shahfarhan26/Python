#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def a(x):
  for i in range(0,len(x)-1):
    if x[i] == 3 and x[i+1] == 3:
      return True
  else :
    return False
