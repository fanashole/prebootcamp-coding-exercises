#Task 9
def multiples(param):
    num = 0
    for i in range(param):
        if(i % 3 == 0) or (i % 5 == 0):  #Looks out for numbers that are divisible by 3 or 5
            num += i
    return num

#Function call
print(multiples(1000))

#Output: 233168