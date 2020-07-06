# R-4.1 Recursive function for finding a max element inside array
def recursive_max(i, j, array):
    if j >= len(array):
        return array[i]
    else:
        if array[j] > array[i]:
            i = j
        return recursive_max(i, j+1, array)


some_array = [3, 2, 5, 1, 4]
max_val = recursive_max(0, 0, some_array)
print(max_val)

# test cases
test_data = [
    ([5, 1, 3, 2, 4], 5),
    ([3, 4, 1, 2, 5], 5),
    ([3, 2, 5, 1, 4], 5),
    ([2, 9, 3, 8, 10, 1], 10),
    ([60], 60)
]

for item in test_data:
    input_item = item[0]
    expected = item[1]
    actual = recursive_max(0, 0, input_item)
    print(input_item, actual, actual == expected)


########################################################################################
# C-4.9 Recursive function to fid a minimum
def find_min_recursive(i, j, the_arr):
    if j >= len(the_arr):
        return the_arr[i]
    else:

        if the_arr[j] < the_arr[i]:
            i = j
        return find_min_recursive(i, j+1, the_arr)


arr = [3, 8, 1, 7]
min_num = find_min_recursive(0, 0, arr)
print(min_num)

####################################################################################


# R-4.2 Recursion trace for the computation of power(2, 5).
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


num = power(2, 5)
print(num)

test_data_2 = [
    [(2, 5), 32],
    [(2, 0), 1],
    [(0, 1), 0],
    [(1, 4), 1],
    [(3, 2), 9]
]

for item_2 in test_data_2:
    input_item_2 = item_2[0]
    expected_2 = item_2[1]
    actual_2 = power(item_2[0][0], item_2[0][1])
    print(input_item_2, actual_2, actual_2 == expected_2)

########################################################################################


# R-4.3 the efficient way of computing power of a number
def power_efficient(x, n):
    if n == 0:
        return 1
    else:
        partial = power_efficient(x, n // 2)  # Divide the power in half every time and recursively stored in partial.
        result = partial * partial
        if n % 2 == 1:              # if n is odd multiply result by x.
            result *= x
        return result


num_2 = power_efficient(2, 18)
print(num_2)

########################################################################################


# R-4.4 the efficient way of computing power of a number
def reverse(s, start, stop):
    if start < stop - 1:                        # if we at least have 2 elements
        s[start], s[stop] = s[stop], s[start]   # swap first and last elements
        reverse(s, start+1, stop-1)


array = [4, 3, 6, 2, 6]
reverse(array, 0, 4)
print(array)

# if we consider start = 0 and stop = to 5, then in the swap we have to write [stop-1]


########################################################################################

# R-4.7 the efficient way of computing power of a number
def convert_str_to_int(st_number, place_val=1):  # place_val: start at 1 then 10, then 100 and so on
    # st_number: the string that we want to convert

    if len(st_number) == 0:                        # iterate through the string if it is empty
        return 0

    else:
        the_last_element = int(st_number[len(st_number) - 1])   # get the last element inside string
        print(the_last_element)
        return the_last_element * place_val + convert_str_to_int(st_number[0:len(st_number) - 1], place_val * 10)
        # 4 * 1 + convert_str_to_int(3 * 10 + convert_str_to_int(....
        # (1 * 1000) + (2 * 100) + (3 * 10) + (4 * 1)


num = convert_str_to_int('1234')
print(num)

# convert_str_to_int('12345')
