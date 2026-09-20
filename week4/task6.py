list=[]


for i in range(0,5):
    j=int(input("Input your whole numbers: "))
    list.append(j)

listmax=list.copy()
listmin=list.copy()

listmax.remove(min(listmax))
listmin.remove(max(listmin))

print(sum(listmax), " ", sum(listmin))
