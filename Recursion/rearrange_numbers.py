# C-4.19 rearrange numbers. evens before odds
def rearrange(i, end, arr):
    if len(arr) == 0:
        return arr
    elif i > end:
        return arr
    else:
        if arr[i] % 2 == 0:
            return rearrange(i + 1, end, arr)
        else:
            odd = arr.pop(i)
            arr.append(odd)
            return rearrange(i, end - 1, arr)


array = [1, 2, 3, 4, 5]
print(rearrange(0, len(array) - 1, array))

array = [2, 5, 6]
print(rearrange(0, len(array) - 1, array))

array = [x for x in range(16)]
print(rearrange(0, len(array) - 1, array))

array = []
print(rearrange(0, len(array) - 1, array))

array = [2, 1]
print(rearrange(0, len(array) - 1, array))

array = [7, 5, 9, 1]
print(rearrange(0, len(array) - 1, array))