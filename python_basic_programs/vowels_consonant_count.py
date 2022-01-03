
string = input("Enter the string: ")
vowels = 0
consonant = 0
for ch in string:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch in "bcdfghjklmnpqrstvwxyz":
        consonant += 1
print("The number of vowels in the given string : "+ str(vowels))
print("The number of consonants in  the given string : "+ str(consonant))


