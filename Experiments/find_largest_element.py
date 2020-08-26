# ######### Find the largest element in array ########
def largest_element(arr):
    if len(arr) == 0:
        return None

    max_num = arr[0]
    for i in range(len(arr)):
        print(i, arr[i])
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num


ar = [90, 69, 23, 120, 180]
print(largest_element(ar))


# ############# Test Cases ##############
test_data = [
    ([1, 45, 23, 5, 67], 67),
    ([-3, -7, 1, 4, 2, -9], 4),
    ([-4, -1, -9, -3], -1),
    ([1, 45, 23, 5, 67, 97, 35], 97),
    ([], None)
]

for item in test_data:
    expected = item[1]
    computed = largest_element(item[0])
    print(expected, computed, expected == computed)
