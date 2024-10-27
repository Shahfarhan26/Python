# Write a function takes a two-word string and returns True if both words begin with same letter
def a(text):
  te = text.lower().split()
  return te[0][0] == te[1][0]
