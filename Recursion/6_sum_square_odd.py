# this function returns the sum of square of odd numbers in the range
def sum_sq_odd(n):
    sum_odd = 0
    for i in range(n):

        if i % 2 != 0:
            sq = i * i
            sum_odd = sum_odd + sq
            # print(sum_odd)
    return sum_odd


num = sum_sq_odd(5)
print(num)

# test the function
test_data = [
    (5, 10),
    (7, 35),
    (0, 0)
]
for test in test_data:
    input_item = test[0]
    expected = test[1]
    actual = sum_sq_odd(input_item)
    print(input_item, expected, actual, expected == actual)
