# Given an integer, print the integer with the order of digits reversed.
from math import log10


def reversed_digits(num):

    range_num = int(log10(num)) + 1
    new_num = 0
    for i in range(range_num):
        f = num % 10
        num = (num - f) // 10

        power = range_num - i - 1
        f = f * (10 ** power)
        new_num = f + new_num
    return new_num


if __name__ == '__main__':
    n = 123456789
    result = reversed_digits(n)
    print(result)