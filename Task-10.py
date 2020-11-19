#Task 10
def string(words):
    vowels = 'aeiouAEIOU'
    print([letter for letter in words if letter in vowels]) #checks and prints lowercase and uppercase vowel characters

#function call
string("PRE bootcamp coding challenges")

#Output: ['E', 'o', 'o', 'a', 'o', 'i', 'a', 'e', 'e']