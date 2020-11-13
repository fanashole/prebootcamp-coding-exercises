#Task 7
#Function that converts celsius to fahrenheit
def convert_to_fahrenheit(c):
    fahrenheit = (c * 9)/5 + 32  #Formula for converting celsius to fahrenheit
    print(int(fahrenheit), "degrees fahrenheit")

convert_to_fahrenheit(30)
#Output:
#86 degrees fahrenheit

#function that converts fahrenheit to celsius
def convert_to_celsius(f):
    celsius = (f-32)*5/9   #Formula for converting fahrenheit to celsius
    print(int(celsius), "degrees celsius")


convert_to_celsius(90)
#Output:
#32 degrees celsius