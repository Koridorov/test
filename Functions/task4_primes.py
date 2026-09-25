def proverka(chislo):
    """This checks whether the number in arg is prime or not"""

    if chislo <= 1:
        return "The number is not prime."

    limit=int(chislo**(1/2)+1)
    
    for i in range(2,limit):
        if (chislo%i==0):
            return "The number is not prime. "

    return "This is a prime number"

p=int(input("Enter the first number in the range you want checked: "))
q=int(input("Enter the last number in the range you want checked: "))

for number in range(p,q+1):
    if (proverka(number))=="This is a prime number":
        print(number, end=" ")