print("Hello")


def is_multiple(n, m):
    for i in range(2, 10):
        # p = m * i
        if n == m * i:
            return True
    return False


multi = is_multiple(6, 3)
print(multi)


