## common element with 2 sets


# def common_element(list_a, list_b):
#     set_1 = set(list_a)
#     set_2 = set(list_b)
#     return set_1.intersection(set_2)
#
# li_a = [5, 1, 3, 2, 3, 4]
# li_b = [3, -2, 0, 8, 3, 2, 4, 3]
# com = common_element(li_a, li_b)
# print(com)


################# use 2 sets
# def common_element(list_a, list_b):
# #     comm = set()
# #     new_set = set()
# #     for i in list_a:
# #         new_set.add(i)
# #     for j in list_b:
# #         if j in new_set:
# #             comm.add(j)
# #     return comm


# uses one set
def common_element(list_a, list_b):
    i = 0
    j = 0
    comm = set()
    while len(list_a) != 0:
        comm.add(list_a.pop())
    while i < len(list_b):
        if list_b[i] in comm:
            i += 1
        else:
            list_b.pop(i)

    comm = set(list_b)
    return comm







li_a = [5, 1, 3, 2, 3, 4]
li_b = [3, -2, 0, 8, 3, 2, 4, 3]
com = common_element(li_a, li_b)
print(com)

################
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
    actual = common_element(item[0], item[1])
    print(expected == actual, expected, actual)

