x = int(input("Enter an integer: "))
ans = 0
while ans * ans * ans < abs(x):
    ans = ans + 1
    print("current guess = ", ans)

if ans * ans * ans != abs(x):
    print(x, "is not a perfect cube")
else:
    if x < 0:
        ans = - ans
    print("cube root of " + str(x) + " is " + str(ans))
