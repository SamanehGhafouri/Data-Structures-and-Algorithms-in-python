# Find smallest kth element in an unsorted array

def smallest_kth_elem(arr, k):
    sort_arr = sorted(arr)
    set_arr = set(sort_arr)
    li_set_arr = list(set_arr)

    for i in range(len(li_set_arr)):
        if len(li_set_arr) < k:
            return "Null"
        elif i == (k - 1):
            return li_set_arr[i]


if __name__ == '__main__':
    ar = [0, 1, 0, 1, 1, 1, 1, 0, 0, 1]
    k = 4
    result = smallest_kth_elem(ar, k)
    print(result)
