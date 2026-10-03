def generateListUntilN(n):
    lst = [2, 3]
    for i in range(2, n + 1):
        ci = lst[i - 1] * lst[i - 2]
        lst.append(ci)
    return lst


print(generateListUntilN(7))