def whole_check(num):
    """This checks whether the number is whole or not"""
    if (num is float) or (num<0):
        print("Please input a whole number. ")
        return False

def prime_check(number:int,checker:int) -> str:
    """This checks whether the number is prime or not"""

    if checker == 2:
        return "This is a prime number"
    if number%(checker-1)==0:
        return "The number is not prime. "
    else: 
        return prime_check(number, checker-1)


number=int(input("Enter a whole number: "))
checker=number
if whole_check(number)!=False:
    print(prime_check(number, checker))