def proverka(chislo):
    """This checks whether the number in arg is prime or not"""

    if chislo <= 1:
        return "The number is not prime."

    limit=int(chislo**(1/2)+1)
    
    for i in range(2,limit):
        if (chislo%i==0):
            return "The number is not prime. "

    return "This is a prime number"

n=int(input("Enter the number you want checked: "))

print(proverka(n))
