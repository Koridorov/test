n=int(input("Please input how many entries in the dictionary 1: "))
dict1=dict()
dictfinal=dict()

for i in range(n):
    j=input("Please enter the key: ")
    k=int(input("Please enter the value: "))
    dict1.update({j:k})

m=int(input("Please input how many entries in the dictionary 2: "))
dict2=dict()

for i in range(m):
    j=input("Please enter the key: ")
    k=int(input("Please enter the value: "))
    dict2.update({j:k})

dictfinal.update(dict1)
dictfinal.update(dict2)

for i in dictfinal.keys():
    if (i in dict1) and (i in dict2):
        dictfinal.update({i:((dict1.get(i))+(dict2.get(i)))})

print(dictfinal)