# a positive int n and returns
# the sum of the square of all the positive integers smaller than n


def sum_square(n):
    sum_of_sq = 0
    for i in range(n):
        sq = i * i
        sum_of_sq = sum_of_sq + sq

    return sum_of_sq


num = sum_square(5)
print(num)

# write a test for the function
test_data = [
    (5, 30),
    (7, 91),
    (0, 0)
]
for test_item in test_data:
    input_item = test_item[0]
    expected = test_item[1]
    # print(input_item, expected)
    actual = sum_square(input_item)
    # print(actual)
    print(input_item, expected, actual, expected == actual)