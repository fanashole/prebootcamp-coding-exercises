#Task 5
import math

def area_of_triangle(x, y, z):
    s = int(x + y + z)/2  #calculating the semi-perimetre
    area = math.sqrt(s*(s - x) * (s - y) * (s - z))  #calculating the area
    print(area)

#function call out
area_of_triangle(20, 10, 20)

'''
Output:
96.82458365518542
'''