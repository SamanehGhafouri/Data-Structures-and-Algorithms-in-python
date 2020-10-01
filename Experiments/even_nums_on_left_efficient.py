def even_nums_on_the_left_efficient(arr):
    i = 0
    j = len(arr) - 1

    while i < j:
        right_val = arr[j]
        left_val = arr[i]
        if left_val % 2 != 0 and right_val % 2 == 0:
            # perform the swap
            temp = right_val
            arr[j] = arr[i]
            arr[i] = temp

            # we can also do this as a swap in python
            # arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif left_val % 2 == 0:
            i += 1
        else:
            j -= 1
    return arr


arr_one = [5, 3, 4, 1, 2]
print(even_nums_on_the_left_efficient(arr_one))


# ################## Test #################### #
test_data = [
    ([4, 2, 0, 3, 1], [1, 2, 3, 0, 4]),
    ([4, 2, 1, 3], [3, 1, 2, 4]),
    ([1, 3, 5], [1, 3, 5]),
    ([5, 3, 1], [5, 3, 1]),
    ([4, 3, 5, 1], [5, 3, 4, 1]),
    ([2, 4, 8, 6, 12, 7], [2, 4, 8, 6, 7, 12]),
    ([2, 6, 4], [2, 6, 4])
]
for item in test_data:
    expected = item[0]
    actual = even_nums_on_the_left_efficient(item[1])
    print(actual == expected, actual, expected)

# ######### Running time = O(n)
# ######### Space complexity = O(1)
