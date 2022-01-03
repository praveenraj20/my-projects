number = int(input("Enter the number: "))
sum = 1
if number == 0:
    print("Enter the valid number for factorial.")
else:
    for i in range(1, number + 1):
        sum = sum * i
    print("The factorial of given number is: ",sum)
sum = 0
for i in range(0,number+1):
    sum = sum + i
print("The sum of given number is: ",sum)