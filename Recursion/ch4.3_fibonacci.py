# Return the nth fibonacci number
# Inefficient implementation of fibonacci numbers
# fibonacci: 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + ....
# Binary recursion and the time complexity is 2 to the n/2 (exponential)
# because each time it calls more than twice


def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-1) + bad_fibonacci(n-2)


# return the 7th number of fibonacci which is 13
num = bad_fibonacci(10)
print(f"The Bad 10th Fibonacci number is: {num}")

# Enter a number to see the series of fibonacci numbers
print(f"Please enter a range that you wanna see Bad fibonacci numbers: ")
to_show = int(input())

if to_show <= 0:
    print("Please enter a positive integer")
else:
    print(f"the Bad Fibonacci sequence of {to_show}th number: ")
    for i in range(to_show + 1):
        print(bad_fibonacci(i))

#######################################################################################################


# Computing the nth Fibonacci number using linear recursion
# we are using the recursion in a way that each invocation makes only one recursive call
# we define a function that returns a pair of consecutive Fibonacci numbers (Fn, Fn-1)
def good_fibonacci(n):

    """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b, a)


num1 = good_fibonacci(10)
print(f"The Good Fibonacci: {num1}")

print(f"Please enter a range for Good fibonacci numbers: ")
to_show_2 = int(input())

if to_show_2 <= 0:
    print("Please enter a positive integer")
else:
    print(f"the Good Fibonacci sequence of {to_show_2}th number: ")
    for j in range(to_show_2 + 1):
        print(good_fibonacci(j))






