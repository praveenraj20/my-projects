s = input("Enter the string: ")
c = input("Enter the Charcter: ")


def count_occurance(s,c):
    string = s.lower()
    char = c.lower()
    count = 0
    for ch in string:
        if ch == char:
            count += 1
    return count


print(count_occurance(s,c))

############## without using function ##############

# s = input("Enter the Sring: ")
# string = s.lower()
# c = input("Enter the Character: ")
# char = c.lower()
# count = 0
# for ch in string:
#     if ch  == char:
#         count += 1
# print("The number of character in the given string is "+ str(count))

