#Task 6
def max_number(x, y, z):
    if x > y and x > z:  #check if x has the largest number
        return(x)
    elif y > x and y > z:  #check if y has the largest number
        return(y)
    elif z > x and z > y:  #check if z has the largest number
        return(z)

#function call
print(max_number(10, 15, 20))
print(max_number(20, 15, 10))
print(max_number(15, 20, 10))
'''
Output:
20
20
20
'''