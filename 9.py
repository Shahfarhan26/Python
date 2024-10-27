"""Return the sum of the numbers in the array, except ignore sections of numbers
starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers."""
def a(x):
  t = 0
  add = True
  for n in x:
    while add :
      if n != 6:
        t += n
        break
      else :
        add = False
    while not add :
      if n != 9 :
        break
      else :
        add = True
        break
  return t
