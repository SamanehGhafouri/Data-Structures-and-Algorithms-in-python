import sys                                                        # Provides getsizeof function
data = []                                                         # Must fix choice of n
for k in range(27):
    a = len(data)                                                 # Number of elements
    b = sys.getsizeof(data)                                       # Actual size of bytes
    print('Length: {0:3}; Size in bytes: {1:4}'.format(a, b))
    data.append(None)                                             # Increase length by one
