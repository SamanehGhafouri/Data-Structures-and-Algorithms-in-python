# print the numbers in this sequence
# [50, 60, 70, 80]
print("the first range is: ")
for i in range(50, 90, 10):
    print(i, end=", ")
print("\n")
#################################################################
# print the numbers in this sequence
# [-8, -6, -4, -2, 0, 2, 4, 6, 8]
print("the second range is: ")
for j in range(-8, 10, 2):
    print(j, end=", ")
print("\n")

##################################################################
# print the list comprehension but first I will do the old way to get that list
# [1, 2, 4, 8, 16, 32, 64, 128, 256]
print("the third range is:")
numbers = []
for i in range(0, 9):
    numbers.append(2**i)
print(numbers)


# print the list comprehension
# [1, 2, 4, 8, 16, 32, 64, 128, 256]
print("the third range using list comprehension is:")
numbers_2 = [2**i for i in range(0, 9)]
print(numbers_2)
