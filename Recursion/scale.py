
arr = [1, 2, 3, 4, 5]
num = 10


# This function multiply the content of the arr by num and return
def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
# make sure that return be out side of the for loop otherwise it only print the first value
    return data


result = scale(arr, num)
print(result)
