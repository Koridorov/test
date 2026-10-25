n=int(input("Please enter your number of items: "))
list1=[]
a=str("")

for i in range (0,n):
    j=(input("Please make an entry to the list: "))
    list1.append(j)

for i in range (0, len(list1)):
    a=a+str(list1[i])

print(a)