#Task 6
def max_number(x, y, z):
    if x > y and x > z:  #check if x has the largest number, if yes then prints x
        print(x)
    elif y > x and y > z:  #check if y has the largest number, if yes then prints y
        print(y)
    elif z > x and z > y:  #check if z has the largest number, if yes then prints z
        print(z)

#function call
max_number(10, 15, 20)
max_number(20, 15, 10)
max_number(15, 20, 10)
'''
Output:
20
20
20
'''