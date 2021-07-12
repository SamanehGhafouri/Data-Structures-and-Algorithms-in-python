# Merge Sort: divide and conquer, it is recursive, very efficient for large data sets
# (log n) merge steps because each merge step doubles the list size
# it does (n) work for each merge step because it must look at every item
# so it runs in O(n log n)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(li):
    if len(li) <= 1:
        return li
    mid = len(li) // 2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])
    return merge(left, right)


if __name__ == '__main__':
    arr = [3, 1, 9, 4, 0, 2, 44, 11, 66, 33, 8, 12, 0, 44, 30, 5, 87, -98]
    res = merge_sort(arr)
    print(res)




