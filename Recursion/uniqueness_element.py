# C-4.11 exercises
# test whether the elements inside an array are unique using for loop


def uniq_elements_for_loop(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return False
    return True                                         # return true if all the elements are unique.


array = [2, 8, 4, 1, 9]
result = uniq_elements_for_loop(array)
print(result)


#############################################################################
# test whether the elements inside an array are unique using recursion. not efficient O(n^2)
def unique_elements_recursion(i, j, ar):                # define 2 indexes i and j in an array of ar

    if i == len(ar) and j == len(ar) + 1:               # if j reached out the end and no equal elements found: True
        return True
    elif j == len(ar):                                  # if j reached the end recursive call
        return unique_elements_recursion(i+1, i+2, ar)  # j = i+1
    elif ar[i] == ar[j]:                                # if same elements found by 2 indexes return False
        return False
    else:
        return unique_elements_recursion(i, j+1, ar)    # otherwise function call


a = [2, 8, 4, 1, 9, 2]
result_2 = unique_elements_recursion(0, 1, a)
print(result_2)


#############################################################################
# test whether the elements inside an array are unique using recursion. efficient way using set
def unique_elements_recursion_w_set(se, i, ar):         # se is a set i as an index into array of ar
    if i == len(ar):                                    # if i reaches the end of array return True
        return True
    if ar[i] in se:                                     # if an element inside the array matches the set. False
        return False
    else:
        se.add(ar[i])                                   # otherwise add elements inside the set and call the function
        return unique_elements_recursion_w_set(se, i+1, ar)


arr = [x for x in range(900)]
arr.append(50)
result_3 = unique_elements_recursion_w_set(set(), 0, arr)
print(result_3)
