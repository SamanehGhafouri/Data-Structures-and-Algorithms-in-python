# C-4.16 reverse a string
def reverse_str(string):
    if len(string) == 0:
        return ''                                       # we cut the first character and put it in
                                                        # the back of the string each time
    else:                                               # call the recursive function on the string except the first
        return reverse_str(string[1:]) + string[0]      # character 'amaneh' + 's' and so on


st = reverse_str('samaneh')
print(st)
