# find letter in a list in O(1)
class FindLetterInBagUsingListMap:

    def __init__(self, characters):
        letter_map = [0 for _ in range(26)]  # initialize a list of 0 to 25 zeroes
        for char in characters:
            index = ord(char) - 97           # each character like 'a'=97 has a number
            letter_map[index] = 1            # if the character in the list return 1 in map list
        self.bag = letter_map

    def is_character_in_bag(self, character):
        return self.bag[ord(character) - 97] == 1


bag_checker = FindLetterInBagUsingListMap(['d', 'b', 'z'])
for char in ['a', 'b', 'c', 'd', 'e', 'y', 'z']:
    print(char, bag_checker.is_character_in_bag(char))


# ------------------------- Test ------------------------------- #
input_data = ['a', 'g', 'z', 'w', 'k', 'b', 'p', 't', 'e']
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

solution = FindLetterInBagUsingListMap(input_data)
for item in test_data:
    expected = item[0]
    actual = solution.is_character_in_bag(item[1])
    print(expected == actual)
