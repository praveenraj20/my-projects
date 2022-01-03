number = int(input("Enter the Number: "))
sum = 0
while number > 0:
    sum = (number%10) + sum * 10
    number = number//10
print("The largest number is: ",sum)