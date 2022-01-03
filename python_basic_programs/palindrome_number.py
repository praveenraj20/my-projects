number = int(input("Enter the number: "))
temp =number
sum = 0
while number > 0:
    sum = (number%10) + sum *10
    number = number//10
if temp == sum:
    print("The given number is palindrome")
else:
    print("The given number is not a palindrome")


