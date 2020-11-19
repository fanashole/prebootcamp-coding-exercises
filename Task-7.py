#Task 7
def convert_to_fahrenheit(c):
    fahrenheit = (c * 9)/5 + 32
    print(int(fahrenheit), "degrees fahrenheit")

convert_to_fahrenheit(30)
#Output:
#86 degrees fahrenheit

def convert_to_celsius(f):
    celsius = (f-32)*5/9
    print(int(celsius), "degrees celsius")


convert_to_celsius(90)
#Output:
#32 degrees celsius