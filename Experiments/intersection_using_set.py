def intersection(list_a, list_b):
    return set(list_a).intersection(list_b)


li_a = [2, 1, 2, 3]
li_b = [2, 3, 5, 2]
print(intersection(li_a, li_b))

# ############## Test ################### #

test_data = [
    ([5, 1, 3, 2, 3, 4], [3, -2, 0, 8, 3, 2, 4, 3], {2, 3, 4}),
    ([-3, 5, -1, 3, 2, 3, -4], [7, 22, 0, 8, 13, 9, 4], set()),
    ([], [5, 2, 3, -3, -4,  -1, 3], set()),
    ([22, 8, 0, 7, 4, 9, 15], [], set()),
    ([22, 8, 0, 7, 4, 9, 15], [5, 2, 3, 0, -4,  -1, 3], {0}),
    ([22, 8, 0, 7, 4, 9, 15], [5, 2, 3, 11, -4,  -1, 22], {22}),
    ([22, 8, -1, 7, 4, 9, 15], [22, 5, 2, 3, 11, -4,  -1], {-1, 22}),
    ([21, 8, -1, 7, 4, 9, 15], [22, 5, 2, 3, 11, -4,  -1, 15], {-1, 15}),
    ([5, 2, 8], [22, 5, 2, 3, 11, -4,  8, 15], {2, 5, 8}),
    ([22, 5, 2, 3, 11, -4,  8, 15], [5, 2, 8], {2, 5, 8})
]

print("--- TESTS ---")
for item in test_data:
    expected = item[2]
    actual = intersection(item[0], item[1])
    print(expected == actual, expected, actual)