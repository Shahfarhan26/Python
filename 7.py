#Given a string, return a string where for every character in the original there are three characters
def a(txt):
  c = ''
  for char in txt:
    c += char*3
  return c
