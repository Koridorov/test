n=int(input("Please input how many entries in the dictionary: "))
dict1=dict()
templist=list()

for i in range(n):
    j=input("Please enter the key: ")
    k=input("Please enter the value: ")
    dict1.update({j:k})

for i in dict1.values():
    if i not in templist:
        templist.append(i)

print(templist)
templist.clear()

