# Insertion sort
def insertion_sort(list_a):
    for i in range(1, len(list_a)):
        while list_a[i - 1] > list_a[i] and i > 0:
            list_a[i - 1], list_a[i] = list_a[i], list_a[i - 1]
            i -= 1
    return list_a

if __name__ == '__main__':
    li = [8, 2, 4, 7, 1, 0, 3, 1]
    result = insertion_sort(li)
    print(result)
