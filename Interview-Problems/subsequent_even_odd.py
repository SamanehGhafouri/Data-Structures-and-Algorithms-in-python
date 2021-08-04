# A string is provided as an input which consists of integer value.
# Insert '*' if subsequent numbers are even and insert '-' if subsequent number are odd.


def subsequent_even_odd(num: str):

    li = []
    for ch in range(len(num) - 1):
        if int(num[ch]) % 2 == 0 and int(num[ch+1]) % 2 == 0:
            li.append(num[ch])
            li.append("*")
        elif int(num[ch]) % 2 != 0 and int(num[ch+1]) % 2 != 0:
            li.append(num[ch])
            li.append("-")
        else:
            li.append(num[ch])
    li.append(num[-1])
    return "".join(li)


if __name__ == '__main__':
    n = "21462675756"
    n2 = "98676555533"
    result = subsequent_even_odd(n)
    print(result)