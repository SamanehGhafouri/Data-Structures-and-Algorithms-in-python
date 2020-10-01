# A number has either an odd parity or an even parity.
# Your function will "sort" all even numbers to the left side of the array,
# and all odd numbers to the right side of the array.


def even_on_the_left(arr):
    arr_1 = []
    arr_2 = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr_1.append(arr[i])
        else:
            arr_2.append(arr[i])
    return arr_1 + arr_2


arr_one = [5, 3, 4, 1, 2]
even_right = even_on_the_left(arr_one)
print(even_right)


# #################### Test ###########################

test_data = [
    ([2, 0, 4, 1, 3], [1, 2, 3, 0, 4]),
    ([2, 4, 3, 1], [3, 1, 2, 4]),
    ([1, 3, 5], [1, 3, 5]),
    ([5, 3, 1], [5, 3, 1]),
    ([4, 5, 3, 1], [5, 3, 4, 1]),
    ([2, 4, 8, 6, 12, 7], [2, 4, 8, 6, 7, 12]),
    ([2, 6, 4], [2, 6, 4])

]

for item in test_data:
    expected = item[0]
    actual = even_on_the_left(item[1])
    print(actual == expected, actual, expected)

# ######### Running time = O(n)
# ######### Space complexity = O(n)
