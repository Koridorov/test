def fibonacci(counter:int):
    if counter==0 or counter==1:
        return counter
    return (fibonacci(counter-1))+(fibonacci(counter-2))


def fibonacci_cycle(counter:int):
    num1=0
    num2=1
    for i in range(0,counter-1):
        if num1<num2:
            num1=num1+num2
        elif num2<=num1:
            num2=num1+num2
    if num1<num2:
        return num2
    return num1


print(fibonacci_cycle(1000))