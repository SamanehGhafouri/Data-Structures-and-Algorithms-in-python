# ### Find the most repeated number in an array ## #
# Time complexity: O(n)
def most_duplicated(arr):
    counts = dict()                     # Initialize an empty dictionary
    for number in arr:                  # It computes the frequency of value in array
        if counts.get(number) is None:
            counts[number] = 1
        else:
            counts[number] += 1

    max_value = 0
    max_key = None
    for key, value in counts.items():   # Get key, value in dictionary and find the max value
        if value > max_value:           # and get the key that corresponds to that max value
            max_value = value
            max_key = key
    return max_key


li = [2, 3, 6, 3, 1]
most_duplicated(li)

# ################### Test Cases ########################## #
test_data = [
    ([2, 3, 6, 3, 1], 3),
    ([5, 2, 3, 1], 5),
    ([2, 2, 2, 2], 2),
    ([1, 1, 3, 4, 5], 1),
    ([6, 2, 3, 3, 3], 3),
    ([1, 6, 9, 9, 5, 9, 4, 5], 9),
    ([-1, 5, 5, 8, 5, 4, 5, 8, 4, -1, 4, 5, 9, -1, 5, -1, 5, 10], 5),
    ([4, 4, 4, 8, 8, 9, 10], 4),
    ([8, 8, 9, 10, 4, 4, 4], 4),
    ([8, 4, 4, 4, 8, 9, 10], 4),
    ([8, 9, 10, 4, 4, 4, 8], 4),
    ([8, 4, 8, 4, 4, 9, 10], 4),
    ([-1, 8, 4, 8, 4, -1, 4, 9, -1, -1, 10], -1),
    ([-1, 5, 5, 8, 5, 4, 5, 8, 4, -1, 4, 5, 9, -1, 5, -1, 5, 10], 5)

]

for item in test_data:
    expected = item[1]
    computed = most_duplicated(item[0])
    print(expected, computed, expected == computed)
