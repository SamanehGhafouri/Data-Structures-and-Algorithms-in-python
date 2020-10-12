def find_intersection_num(list_a, list_b):
    new_set = set()
    intersect_nums = set()

    for i in list_a:
        new_set.add(i)

    for j in list_b:
        if j in new_set:
            intersect_nums.add(j)
    return intersect_nums


li_a = [5, 1, 3, 2, 3, 4]
li_b = [3, -2, 0, 8, 3, 2, 4, 3]
print(find_intersection_num(li_a, li_b))



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
    actual = find_intersection_num(item[0], item[1])
    print(expected == actual, expected, actual)
