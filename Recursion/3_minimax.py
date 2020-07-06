arr = [50, 900, 1, 700, 30, 20, 8]


def mi_max(nums):
    maxim = nums[0]
    for i in range(len(nums)):

        if nums[i] > maxim:
            maxim = nums[i]
            nums[i] = nums[i] + 1
    return maxim


nu = mi_max(arr)

print(f"the max is: {nu}")

# test_data
test_data = [
    ([50, 0, 1, 7, 30, 20, 8], 50),
    ([4, 20, 40, 1, 10], 40),
    ([4, 10, 1, 3, 90], 90)
]
# test driver
for test_item in test_data:
    input_item = test_item[0]
    expected = test_item[1]
    # print(input_item, expected)
    actual = mi_max(input_item)
    # print(actual)
    print(input_item, expected, actual, expected == actual)



