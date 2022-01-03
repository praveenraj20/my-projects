#---------- to get input from the user in array -----------#

# from array import *
# arr = array("i",[])
# x = int(input("enter the length of array: "))
# for i in range(x):
#     n = int(input("enter the element: "))
#     arr.append(n)
# print(arr)

#-------------- Count Occurance in Array ------------------#

# from array import  *
# num = array("i",[1,2,34,5,61,1,3,4,1,1])
# # for i in num:
# print(num.count(1))

#------------------ array maths_functions _______________#

# from numpy import array
# arr = array[1,2,3,4,50]
# div = arr/2
# print(div)

#---------------- largest number in Array ---------------#

# from array import *
#
# def largest_num(arr,n):
#     max = arr[0]
#     for i in range(1,n):
#         if arr[i] > max:
#             max = arr[i]
#     return  max
#
#
# arr = array("i",[2,3,4,99,22,33,44,12,5,55,1])
# n= len(arr)
# print("the largest number in array is: ", largest_num(arr,n))
# print(n)
# print(arr.index(1))

#------------------------- array comparison -------------------------------#

# from array import*
#
# arr = array("i",[1,2,3,4,5])
# arr_b = array("i",[1,2,3,4,5,6,7,8,9,10])
# arr_c = array("i",[])
# i = 0
# l = len(arr_b)
# for i in range(1,l):
#     if arr_b[i] not in arr:
#         arr_c.append(arr_b[i])
#         i += 1
# print(arr_c)

#----------------- reverse an array -------------------#

# from array import*
#
# arr = array("i",[1,2,3,4,5])
# result = arr[::-1]
# print(result)

#-------------------- method_2 to reverse an array -------------#

# from array import*
# arr = array("i",[1,2,3,4,5,9,7,8])
# reverse = array("i",[])
# l = len(arr)
# for i in range(l-1,-1,-1):
#     reverse.append(arr[i])
# print(reverse)

#------------------- sort an array (ass & des) -----------------#

from array import *
arr = array("i",[9,2,4,1,8,10,3,7,5,6])
l =len(arr)
for i in range(l):
    for j in range(i+1,l):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)
for i in arr:
    print(i,end=" ")

