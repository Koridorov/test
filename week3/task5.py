a=int(input("First number: "))

b=int(input("Second number: "))

c=int(input("Third number: "))

largest=a
smallest=a

if largest<b:
    largest=b
elif largest<c:
    largest=c
print(f"Largest {largest}")

if smallest>b:
    smallest=b
elif smallest>c:
    smallest=c
print(f"Smallest {smallest}")

if (a>b and a<c) or (a<b and a>c):
    mid=a
elif (b>a and b<c) or (b<a and b>c):
    mid=b
else:
    mid=c
print(f"Middle {mid}")