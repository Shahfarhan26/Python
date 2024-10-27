"""BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
return their sum. If their sum exceeds 21 and there's an eleven, 
reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST"""
def jack(x,y,z):
  sum = x + y + z
  if sum <= 21 :
    return sum
  elif 11 in [x,y,z] and sum <= 31:
    sum = sum - 10
    return sum
  else :
    return "bust"
