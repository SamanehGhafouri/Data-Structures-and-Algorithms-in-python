# given a set of letters, find if a letter is inside of the set in O(1)
def find_letter_in_set(input_letter, letters):
    if input_letter not in letters:
        return False
    return True


letters = {'a', 'g', 'z', 'w', 'k', 'b', 'p', 't', 'e'}
in_letter = 'g'
find_one = find_letter_in_set(in_letter, letters)




print(find_one)

# ------------------------- Test ------------------------------- #
input_data = {'a', 'g', 'z', 'w', 'k', 'b', 'p', 't', 'e'}
test_data = [
    (True, 'k'),
    (True, 'b'),
    (False, 'c'),
    (False, 'd'),
    (True, 'e'),
    (False, 'f'),
    (True, 'g'),
    (False, 'h'),
    (True, 'z'),
    (False, 'i'),

]

for item in test_data:
    expected = item[0]
    actual = find_letter_in_set(item[1], input_data)
    print(expected == actual)


