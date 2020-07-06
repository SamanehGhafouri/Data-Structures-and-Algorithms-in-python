# R-4.5 recursion trace for execution of function puzzle_solve
from copy import copy

counter = 0                                 # To count the number of sets


def puzzle_solve(empty_s, u):
    global counter
    for element in range(len(u)):

        empty_s_copy = copy(empty_s)        # Make a copy of our empty array
        u_copy = copy(u)                    # Make a copy of our array with elements

        empty_s_copy.append(u[element])     # Add elements from u to empty array
        u_copy.pop(element)                 # Remove elements from back of u

        if len(u_copy) == 0:                # If the copy of u is empty in other words, we reach the end of the tree
            counter += 1
            print(empty_s_copy)
        else:
            puzzle_solve(empty_s_copy, u_copy)


puzzle_solve([], ['a', 'b', 'c'])
print("counter: ", counter)


