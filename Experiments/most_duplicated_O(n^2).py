

# ### Find the most repeated number in an array ## #
# The time complexity is O(n^2)
def most_frequent_num(arr):
    if len(arr) == 0:
        return 0

    most_rep_num = arr[0]
    most_rep_num_count = arr.count(arr[0])

    for num in arr:
        if arr.count(num) > most_rep_num_count:
            most_rep_num_count = arr.count(num)
            most_rep_num = num

    return most_rep_num, most_rep_num_count


lis =[1, 2, 2, 2, 3, 5, 2, 1]
print(most_frequent_num(lis))
liss = [0]
print(most_frequent_num(liss))

# ############ Test ############## #
test_data = [
    ([1, 2, 2, 2, 3, 5, 2, 1], 2, 4),
    ([8, 3, 2, 8, 3, 3, 2, 8, 3, 3], 3, 5),
    ([9, 1, 3, 1, 9, 1, 2, 1, 2], 1, 4),
    ([0, 0, 1, 3, 0], 0, 3),
    ([0], 0, 1),
    ([5, 5, 5, 5], 5, 4)

]

for item in test_data:
    expected = item[1], item[2]
    actual = most_frequent_num(item[0])
    accurent = item[2]
    print(f"Has test passed? {expected == actual}")


