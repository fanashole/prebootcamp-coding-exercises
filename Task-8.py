import math

def convert(num):
    hour = math.floor(num / 60)  #calculates hours and leaves the remainder
    minutes = num % 60  #calculates the remainder and turns them into minutes
    if hour == 1 and minutes > 1:
        print(hour, "hour", minutes, "minutes")
    elif hour == 1 and minutes == 1:
        print(hour, "hour", minutes, "minute")
    elif hour > 1 and minutes == 1:
        print(hour, "hours", minutes, "minute")
    else:
        print(hour, "hours", minutes, "minutes")

#function call
convert(500)
convert(110)
convert(121)


'''
Output:
8  hours 20 minutes
1  hour 50 minutes
2 hours 1 minute
'''




