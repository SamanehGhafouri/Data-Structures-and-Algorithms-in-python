# Reverse a string without using built in function
# Using recursion

def reverse(string):
    if len(string) == 0:
        return string
    else:
        # call reverse function on substring and add the first ch to the end of the string
        return reverse(string[1:]) + string[0]


if __name__ == '__main__':
    s = "Hello World"
    result = reverse(s)
    print(result)