string = input("enter the string: ")


def reverse_string():
    reverse = ""
    for ch in string:
        reverse = ch + reverse
    return reverse


print("the reverse string is", reverse_string())


#### without using for loop ###

# string = input("Enter the string: ")
#
#
# def reverse_string():
#     result = string[::-1]
#     return result
#
#
# print(reverse_string())

