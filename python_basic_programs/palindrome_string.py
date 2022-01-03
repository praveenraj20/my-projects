string = input("Enter the String: ")


def is_palindrome(para):
    rev_string = string[::-1]
    return rev_string == string


print(string+ " is palindrome", is_palindrome(string))










