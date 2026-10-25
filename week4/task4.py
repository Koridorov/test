n=int(input("Please enter your number of items: "))
list1=[]
list2=[]
listfinal=[]

for i in range (0,n):
    j=input("Please enter the items for the first list: ")
    list1.append(j)
for i in range (0,n):
    j=input("Please enter the items for the second list: ")
    list2.append(j)

for i in list1:
    if i in list2:
        listfinal.append(i)

print(listfinal)