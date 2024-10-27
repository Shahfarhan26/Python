#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old(text):
  a = text[0]
  b = text[1:4]
  c = text[4]
  d = text[5:]
  return a.lower() + b + c.lower() + d
