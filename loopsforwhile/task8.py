n=int(input("Enter the number you want checked: "))
x=int(n**(1/2)+1)
for i in range(2,n):
    if n%i==0:
        print("This is not a prosto chislo. ")
        break
    elif (n%i!=0) and (i==(n-1)):
        print("This is a prosto chislo")
        break