n=int(input("Please input how many entries you would like to enter: "))
tuple1=()
for i in range(n):
    j=(input("Input the entry: "))
    tupletemp=(j,)
    tuple1=tuple1+tupletemp
    tupletemp=list(tupletemp)
    tupletemp.clear()
if (len(tuple1))==3:
    el1,el2,el3=tuple1
    print(el1, el2, el3, type(tuple1))

k=input("Please input the additional entry: ")
listtemp=list(tuple1)

listtemp.insert(int((len(listtemp))//2), k)
tuple2=tuple(listtemp)
print(tuple2, type(tuple1))

listtemp=list(tuple2)
listtemp.pop()
listtemp.pop()
tuple3=tuple(listtemp)
tuple3=tuple3*5
print(tuple3)