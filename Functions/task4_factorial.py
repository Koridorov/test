def factorial(number:int):
    total=1
    for i in range(2,number+1):
        total*=i

    return total


n=int(input("Enter a number: "))

print(factorial(n))