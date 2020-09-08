# Must find exactly one integer in A and one integer in B such that their sum is equal to T
def find_sum_in_two_lists(list_a, list_b, t):
    set_b = set(list_b)                          # store list_b in a set make the code efficient
    for i in list_a:
        if t - i in set_b:                       # because finding element inside set takes O(1)
            b = t - i                            # If list_b was used finding elements would take O(n)
            return i, b
    return None


A = list(range(1, 5000, 2))
B = list(range(100*3000))
print(find_sum_in_two_lists(A, B, 100*2999 + 2548))

# ############### TEST ######################
test_data = [
    ([2, 2, 3], [4, 5, 6], 8, (2, 6)),
    ([2, 2, 3], [5, 6, 1], 6, None),
    ([], [4, 5, 6], 5, None),
    ([0], [4, 5, 6], 5, (0, 5)),
    ([0], [4, 5, 6], 9, None)
]

for item in test_data:
    expected = item[3]
    actual = find_sum_in_two_lists(item[0], item[1], item[2])
    print(expected == actual, expected, actual)
