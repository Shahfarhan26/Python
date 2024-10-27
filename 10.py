#Write a function that takes in a list of integers and returns True if it contains 007 in order.
def spy_game(nums):
    testlist = []
    string = ""
    for i in nums:
        if i == 0 or i == 7:
            testlist.append(i)
    for i in testlist:
        string += str(i)
    if "007" in string:
        return True
    else:
        return False 
