n=int(input("Enter the number you want checked: "))
x=int(n**(1/2)+1)
for i in range(2,x):
    if n%i==0:
        print("This is not a prime number. ")
    elif (n%i!=0) and (i==(x-1)):
        print("This is a prime number")
