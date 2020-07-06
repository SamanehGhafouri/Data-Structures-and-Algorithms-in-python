print("Please enter the number you wish to see the factorial: ")
user = int(input())


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


fac_num = factorial(user)
print(f" the total factorial of 5 is: {fac_num}")


# #################### Recursive factorial function ############ #
def fact(n):

    if n == 0:
        return 1
    else:
        return n * fact(n-1)


num = fact(1000)
print(num)


# #################### Iterative factorial function ################## #
def factorial(n):
    # accumulator
    fac = 1
    for i in range(1, n + 1):
        fac = i * fac
    return fac


# Capture the functions return value
result = factorial(4)
print(result)
