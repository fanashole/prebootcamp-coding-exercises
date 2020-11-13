#Task three
def number(a, b):
    if a == 65 or b == 65 or (a + b) == 65:  #check if either number is 65 or total sum of numbers is 65
        return True
    else:
        return False

#Printing the function call out
print(number(65, 40))
print(number(21, 10))
print(number(50, 15))

'''
Output:
True
False
True
'''
