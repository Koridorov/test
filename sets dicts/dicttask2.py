n=int(input("Please input how many entries in the dict: "))
keys=list()
values=list()
for i in range(n):
    j=input("Please enter your key: ")
    keys.append(j)

for i in range(n):
    j=input("Please enter your value: ")
    values.append(j)

dict1=dict()
for i in range(n):
    dict1.update({(keys[i]):(values[i])})

for item in dict1.items():
    print(item)