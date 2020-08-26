# ############ Find the minimum number in an array ############# #
def find_smallest(arr):
    if len(arr) == 0:
        return None

    smallest = arr[0]
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest


ar = [90, 69, 23, 120, 180]
print(find_smallest(ar))


# ############# Test Cases ##############
test_data = [
    ([1, 45, 23, 5, 67], 1),
    ([-3, -7, 1, 4, 2, -9], -9),
    ([-4, -1, -9, -3], -9),
    ([1, 45, 23, 5, 67, 97, 35], 1),
    ([], None)
]

for item in test_data:
    expected = item[1]
    computed = find_smallest(item[0])
    print(expected, computed, expected == computed)
