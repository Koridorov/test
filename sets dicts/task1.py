n=int(input("Enter how many strings you would like to input: "))
set1=set()

for i in range(n):
    j=str(input("Please enter the string: "))
    set1.add(j)
#print(set1)
set2=set1.copy()
#for item in set2:
#    if "asd" in item:
#        set1.remove(item)
#print(set1)

set2.clear()
m=int(input("Enter the number M: "))
for i in range(m):
    j=str(input("Please enter the string: "))
    set2.add(j)
if set2.issubset(set1):
    set3=set1.difference(set2)
elif set1.issubset(set2):
    set3=set1.difference(set2)
else:
    set3=set1.union(set2)
print(set3)

if ("asd") in set3:
    set3.remove("asd")
else:
    set3.add("asd")
if ("123") in set3:
    set3.remove("123")
else:
    set3.add("123")
if ("fmi") in set3:
    set3.remove("fmi")
else:
    set3.add("fmi")
print(set3)

k=int(input("Please enter the number K: "))
set4=set()
for i in range(k):
    j=str(input("Please enter the string: "))
    set4.add(j)

print(set4.intersection(set3))