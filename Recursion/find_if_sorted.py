arr = [2, 3, 4, 6, 900]
arr2 = [900, 2, 3, 4, 6]
arr3 = [2, 7, 1, 90, 8]


# finding if the array is sorted
def if_sorted(data):

    # for i in range(len(data) - 1):
    #     if data[i] > data[i+1]:
    #         return False
    # return True
    for i in range(len(data) - 1):
        if data[i] < data[i+1]:
            continue
        else:
            return False
    return True

# num = if_sorted(arr)
# print(num)


# test the function
test_data = [
    (True, [2, 3, 4, 6, 900]),
    (False, [900, 2, 3, 4, 6]),
    (False, [2, 7, 1, 90, 8]),
    (False, [1, 3, 70, 7]),
    (True, [1]),
    (True, [])
]


for item in test_data:
    expected = item[0]
    actual = if_sorted(item[1])
    print(f"Has test passed? {expected == actual}")









