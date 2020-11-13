
#Task 11
def characters(first, second):
    set1 = set(first)
    set2 = set(second)
    set3 = (set1 & set2)
    msg = ''.join(set3)
    return msg

first = "codecamp"  #first input
second = "bootcamp"  #second input
find_characters = characters(first, second)
print(find_characters)

#Output:
# pcoma