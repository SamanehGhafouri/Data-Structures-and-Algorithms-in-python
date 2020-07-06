print("Welcome to the program of determining if a number is even or not!")
print("Please enter a number: ")

num = int(input())


def is_even(k):
    if k % 2 == 0:
        return True
    return False


even = is_even(num)
print(even)







