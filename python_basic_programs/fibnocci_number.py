n = int(input("number: "))
num_1 = 0
num_2 = 1
for i in range(n):
    print(num_1)
    temp = num_1
    num_1 = num_2
    num_2 = temp + num_2



