# inefficient palindrome O(2n)                  # If the reverse is equal to the string is palindrome
def palindrome_2n(name):
    name_r = reverse_name(name)
    if name == name_r:
        return name
    else:
        return None


def reverse_name(nam):                          # Get the reverse of a string
    if len(nam) == 0:
        return ''
    else:
        return reverse_name(nam[1:]) + nam[0]


n = palindrome_2n('racecar')
print(n)


#####################################################################################
# Efficient way palindrome with O(n)
def palindrome_n(i, j, string):
    if j <= i:
        return True
    elif string[i] != string[j]:
        return False
    else:
        return palindrome_n(i+1, j-1, string)


input_name = 'racecar'
name_input= palindrome_n(0, len(input_name)-1, input_name)
print(name_input)
if name_input is True:
    print(input_name)
else:
    print("No not palind")




