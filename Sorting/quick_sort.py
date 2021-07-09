# Quick sort
# Complexity: worst case O(n^2) and average case O(nlogn)
# How it works: pick a pivot and make 2 lists: 1 list has numbers less than the pivot and the other list
# has numbers greater than the pivot. This process continues till all the numbers sorted
def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    else:
        # return the last element
        pivot = arr.pop()
        item_greater = []
        item_lower = []
        for item in arr:
            if item > pivot:
                item_greater.append(item)
            else:
                item_lower.append(item)
        return quick_sort(item_lower) + [pivot] + quick_sort(item_greater)


if __name__ == '__main__':
    ar = [8, 2, 10, 3, 88, 29, 93, 2, 4, 5, 0]
    result = quick_sort(ar)
    print(result)

