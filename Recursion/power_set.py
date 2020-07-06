# C-4.15 computing the power set
def power_set(the_set):

    if len(the_set) == 0:
        return [[]]

    else:
        # x = power_set(the_set[1:])
        # print(f"the x is: {x}")
        # print(f"the set[0]: {[[the_set[0]]]}")
        # for y in x:
        #     print(f"the y is: {y}")
        #     print(f"final result: {x + [[the_set[0]] + y for y in x]}")

        return sorted(power_set(the_set[1:]) + [[the_set[0]] + i for i in power_set(the_set[1:])])


st = [1, 2, 3]
result = power_set(st)
print(result)
