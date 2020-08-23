import ctypes                                           # provides low level arrays


class DynamicArray:
    """ A dynamic array class akin to a simplified python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0                                     # count actual elements
        self._capacity = 1                              # Default array capacity
        self._A = self._make_array(self._capacity)      # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        # if k < 0:
        #
        #     target_index = k * (-1)
        #     target_index = target_index % self._n
        #     if target_index > 0:
        #         target_index = self._n - target_index
        #     return self._A[target_index]

        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]                              # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:                   # not enough room
            self._resize(2 * self._capacity)            # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                                # nonpublic utility
        """Resize internal array to capacity c."""
        B = self._make_array(c)                         # new (bigger) array
        for k in range(self._n):                        # for each existing value
            B[k] = self._A[k]
        self._A = B                                     # use the bigger array
        self._capacity = c

    def _make_array(self, c):                           # nonpublic utility
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this version)
        if self._n == self._capacity:                   # not enough room
            self._resize(2 * self._capacity)            # so double capacity
        for j in range(self._n, k, -1):                 # shift rightmost first
            self._A[j] = self._A[j - 1]
        self._A[k] = value                              # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value(or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:                     # found a match!
                for j in range(k, self._n - 1):         # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None             # help garbage collection
                self._n -= 1                            # we have one less item
                return                                  # exit immediately
        raise ValueError('value not found')         # only reached if no match


# test insert function
test_data =[
    ([1, 2, 3], 0, 5, [5, 1, 2, 3])
]

for item in test_data:
    expected = item[3]

    dy_arr = DynamicArray()
    for num in item[0]:
        dy_arr.append(num)

    dy_arr.insert(item[1], item[2])
    actual = []
    for i in dy_arr:
        actual.append(i)

    print(actual == expected, actual, expected)

################################################################


# test remove function
# test_data2 = [
#     ([1, 2, 3, 4], 1, [2, 3, 4]),
#     ([1, 2, 3, 4], 2, [1, 3, 4]),
#     ([1, 2, 3, 4], 4, [1, 2, 3]),
#     ([1, 2, 3, 4], 5, 'not found')
#
#
# ]
#
# for item in test_data2:
#     expected = item[2]
#
#     dy_arr = DynamicArray()
#     for num in item[0]:
#         dy_arr.append(num)
#     dy_arr.remove(item[1])
#     actual = []
#     for i in dy_arr:
#         actual.append(i)
#
#     print(actual == expected, actual, expected)







