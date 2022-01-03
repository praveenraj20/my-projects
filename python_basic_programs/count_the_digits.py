number = int(input("enter the numbers: "))
count = 0
while number > 0:
    number = number//10
    count += 1
print(count)
