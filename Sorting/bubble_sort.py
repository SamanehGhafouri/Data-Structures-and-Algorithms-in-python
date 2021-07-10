# Bubble sort: takes an unsorted list and sort it in ascending order
# lowest value at the beginning by comparing 2 elements at a time
# this operation continues till all the elements are sorted
# we have to find the breaking point
# Time Complexity: best case: O(n)
#                  average and worst case: O(n^2)

def bubble_sort(li):
    sorted_li = False

    while not sorted_li:
        sorted_li = True
        for i in range(len(li) - 1):
            if li[i] > li[i+1]:
                sorted_li = False
                li[i], li[i+1] = li[i+1], li[i]
    return li


if __name__ == '__main__':
    l = [9, 3, 1, 6, 8, 22, 0]
    result = bubble_sort(l)
    print(result)