n=int(input("Enter how many numbers you would like to see: "))
num1=0
num2=1
print(num2, end=" ")
for i in range(0,n-1):
    num1=num1+num2
    print(num1, end=" ")

    num2=num1+num2
    print(num2, end=" ")