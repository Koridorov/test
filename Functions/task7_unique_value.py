def unikat(lst:list):
    return list(dict.fromkeys(lst))

lst=[1, 2, 1, 3, 1, 4]

print(unikat(lst))