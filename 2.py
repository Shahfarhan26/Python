#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(x,y):
  if (x + y) == 20 or x == 20 or y == 20:
    return True
  else :
    return False
