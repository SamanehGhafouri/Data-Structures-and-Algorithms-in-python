def fizz_buzz_game(n):
    list_num = []
    for i in range(1, n+1):
        if i % (3 * 5) == 0:
            list_num.append("FizzBuzz")
        elif i % 3 == 0:
            list_num.append("Fizz")
        elif i % 5 == 0:
            list_num.append("Buzz")
        else:
            list_num.append(str(i))
    return list_num


num = 15
list_a = fizz_buzz_game(num)
print(list_a)

# ############## TEST #################################

test_data = [
    (15,  ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
           "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]),
    (3, ["1", "2", "Fizz"]),
    (5, ["1", "2", "Fizz", "4", "Buzz"]),
    (30, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
          "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
          "16", "17", "Fizz", "19", "Buzz", "Fizz","22", "23",
          "Fizz", "Buzz", "26", "Fizz", "28", "29", "FizzBuzz"])
]
for item in test_data:
    expected = item[1]
    actual = fizz_buzz_game(item[0])
    print(expected == actual, expected, actual)
