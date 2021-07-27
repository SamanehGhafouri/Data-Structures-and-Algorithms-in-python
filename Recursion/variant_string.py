# find the variant of a string
# the number of variant of the string
# the number of distinct variant of the string

global count
count = 0


def variant_of_a_string(final: list, given: list, distinct_final: set):
    global count
    if len(given) == 0:
        count += 1
        print(" ".join(final))
        distinct_final.add(" ".join(final))
    else:
        for i in range(len(given)):
            copy_given = given.copy()
            char = copy_given.pop(i)
            variant_of_a_string(final + [char], copy_given, distinct_final)


if __name__ == '__main__':
    str = "Samaneh"
    str_li = []
    str_li[:] = str
    dist_fin = set()
    result = variant_of_a_string([], str_li, dist_fin)
    print(result)
    print(count)
    print(dist_fin)
    print(len(dist_fin))

