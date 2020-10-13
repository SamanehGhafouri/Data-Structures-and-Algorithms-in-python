def reverse_number(num):
    reverse = 0
    while num > 0:
        remainder = num % 10                    # Get the remainder by dividing the number by 10
        reverse = (reverse * 10) + remainder
        num = num / 10                          # After we get the first digit reversed, divide the number by 10
    return reverse                              # to eliminate the first digit and so on


n = 201
print(reverse_number(n))


# ################# TEST ################# #

test_data = [
    (0, 0),
    (102, 2010),
    (4901, 1094),
    (69, 96),
    (12012, 21021),
    (999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     9999999999999999999999999999999999999991,
     1999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999 /
     999999999999999999999999999999999999999
     )
]

for item in test_data:
    expected = item[0]
    actual = reverse_number(item[1])
    print(expected == actual, expected, actual)