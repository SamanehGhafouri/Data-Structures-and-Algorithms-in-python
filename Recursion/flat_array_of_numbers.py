# given an array containing numbers and possible sub-arrays
# of numbers, recursively, write a function that turns a flat
# array of numbers


def flat_arr(arr):
    li = []
    for i in arr:
        if type(i) != int:
            li.extend(flat_arr(i))
        else:
            li.append(i)
    return li


ari = [[1, 2, 3], [4, 5, 6]]
func = flat_arr(ari)
print(func)

ari = [1,[2,[3,4],5],[6,7]]
flat_ari = flat_arr(ari)
print(flat_ari)


# ------------------------- Test ------------------------------ #

test_data = [
    ([1, 2, 3, 4, 5, 6, 7], [1, [2, [3, 4], 5], [6, 7]]),
    ([1, 2, 3, 4, 5, 6], [[1, 2, 3], [4, 5, 6]]),
    ([4, 7, 2, 5, 1], [4, [[7, 2], 5], 1]),
    ([4, 6, 1, 5, 2, 8, 9, 3, 4, 2], [4, [[6, [[1, [5, 2]], 8, 9], 3], 4, 2]])

]

for item in test_data:
    expected = item[0]
    actual = flat_arr(item[1])

    print(expected == actual, expected, actual)