#Task four
import re

def numbers(x, y):
    if x == 3 or y == 3 and re.search("3",str(x+y)) :

        return True
    else:
        return False

#Printing the function call out
print(numbers(3, 10))
print(numbers(11, 3))
print(numbers(20, 3))
print(numbers(5, 8))

'''
Output:
True
False
True
False
'''
