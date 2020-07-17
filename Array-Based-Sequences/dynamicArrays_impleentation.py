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
        if k < 0:

            target_index = k * (-1)
            target_index = target_index % self._n
            if target_index > 0:
                target_index = self._n - target_index
            return self._A[target_index]

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
        return (c * ctypes.py_object)()                 # see ctypes documentation


test_data =[
    (3, 2, [1, 2, 3, 4]),
    ('Exception', 3 , [1, 2, 3]),
    (4, -1, [1, 2, 3, 4]),
    (3, -2, [1, 2, 3, 4]),
    (1, -4, [1, 2, 3, 4]),
    (5, -1, [1, 2, 3, 4, 5]),   # ei = 4, gi = 1
    (1, -20, [1, 2, 3, 4, 5]),  # ei = 0, gi = 0
    (3, -18, [1, 2, 3, 4, 5]),  # ei = 2, gi = 3
    (1, -5**5000000, [1, 2, 3, 4, 5])
]

for item in test_data:
    expected = item[0]
    input_index = item[1]
    input_arr = item[2]

    dy_arr = DynamicArray()
    for num in input_arr:
        dy_arr.append(num)

    # my way of handling exceptions
    if expected == "Exception":
        exception_caught = False
        try:
            actual = dy_arr[input_index]
        except:
            exception_caught = True

        if exception_caught:
            print("PASS: Exception Raised")
        else:
            print("FAILED: Exception NOT Raised")

    else:
        actual = dy_arr[input_index]
        print(actual == expected, actual, expected)