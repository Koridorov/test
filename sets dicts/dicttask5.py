string=input("Please enter the string: ")
dict1=dict()
listtemp=list()
for word in (string.split()):
    listtemp.append(word.lower())

for word in listtemp:
    dict1.update({word:listtemp.count(word)})

listtemp.clear()
print(dict1)
