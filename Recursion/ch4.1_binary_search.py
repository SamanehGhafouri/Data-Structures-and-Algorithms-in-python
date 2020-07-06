arr = [2, 5, 6, 8, 10, 12, 14, 16]


# low and high are both indexes, data is a list or an array
def binary_search(data, target, low, high):
    # compare if the list is sorted
    if low > high:
        return False
    else:
        # in this example low = 0 and high = 8
        # 0+8/2= 4 we usually consider the lower bound
        # data[4] = 10
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


num = binary_search(arr, 5, 0, 7)
print(num)

# ## Writing tests ##### #
test_data = [
    (True, [2, 5, 6, 8, 10, 12, 14, 16], 10),
    (True, [2, 5, 6, 8, 10, 12, 14, 16], 2),
    (True, [2, 5, 6, 8, 10, 12, 14, 16], 16),
    (True, [2, 5, 6, 8, 10, 12, 14, 16], 5),
    (True, [2, 5, 6, 8, 10, 12, 14, 16], 14),
    (False, [16, 7, 28, 19, 40, 2], 6,),
]


for item in test_data:

    expected = item[0]
    actual = binary_search(item[1], item[2], 0, len(item[1]))
    print(f"Test Result: {expected == actual} : expected: {expected}, actual: {actual}")

