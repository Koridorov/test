def whole_check(num):
    """This checks whether the number is whole or not"""
    if (num is float) or (num<=0):
        print("Please input a whole number. ")
        return False

def recursive_factorial(num:int) -> int:
    """This finds the factorial using a recursive function"""
    if num==1:
        return num
    return num*recursive_factorial(num-1)
    


number=int(input("Enter a whole number: "))
total=1
if whole_check(number)!=False:
    print(recursive_factorial(number))