#MASTER YODA: Given a sentence, return a sentence with the words reversed
def yoda(text):
  a = text.split()
  b = a[::-1]
  return ' '.join(b)
