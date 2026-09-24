n=int(input("Please enter how many items you would like to enter: "))
dict1=dict()
dict2=dict()
for i in range (n):
    j=(input("Please enter the key you would like to input: "))
    k=input("Please enter the value you would like to input: ")
    if j not in dict1.keys():
        dict1.update({j:k})
    else:
        print("The key already exists and will not be saved.")
print(dict1)

m=int(input("Please enter how many items you would like to enter: "))
for i in range (n):
    j=(input("Please enter the key you would like to input: "))
    k=input("Please enter the value you would like to input: ")
    dict2.update({j:k})
print(dict2)

resultdict=dict()
resultdict.update(dict1)
resultdict.update(dict2)

print(resultdict)
stringtemp=str()
for item, value in resultdict.items():
    stringtemp+=value
print(stringtemp)

dicttemp=resultdict.copy()

for item, value in dicttemp.items():
    if item==value:
        resultdict.pop(item)

dicttemp.clear()

print(resultdict)