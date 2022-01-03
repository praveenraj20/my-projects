numbers = [1,2,3,4,56,65,5,4]
output = []
dublicate = []
for num in numbers:
    if num in output:
        dublicate.append(num)
    if num not in output:
        output.append(num)
print(str(output) + " and the dublicate numbers is " + str(dublicate))
