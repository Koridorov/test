from functools import reduce

def fibonacci_map(number:int) -> list:
    """This calculates the first N numbers of the fibonacci sequence"""
    num1=0
    num2=1
    lst=[num1, num2]
    for num in range ((number-1)//2):
        if num1>=num2:
            num2=num1+num2
            lst.append(num2)
        if num2>num1:
            num1=num1+num2
            lst.append(num1)
    #return list(map(lambda x: x**2, lst))
    return lst

def prime_checker(num:int):
        x=int(num**(1/2)+1)
        for i in range(2,x):
            if num%i==0:
                return False
            elif (num%i!=0) and (i==(x-1)):
                return True

prime_fibonacci=list(filter(lambda x: prime_checker(x), fibonacci_map(10)))
even_fibonacci_squared=list(filter(lambda x: x>0 and x%2==0, list(map(lambda x: x**2, fibonacci_map(10)))))

prime_fibonacci_sum=reduce(lambda x,y: x+y, prime_fibonacci)
even_fibonacci_squared_sum=reduce(lambda x,y: x+y, even_fibonacci_squared)

print(prime_fibonacci_sum if prime_fibonacci_sum > even_fibonacci_squared_sum else even_fibonacci_squared_sum)
#print(filter(lambda x,y: x>y, (reduce((lambda x, y: x + y), prime_fibonacci), reduce((lambda x, y: x + y), even_fibonacci_squared))))