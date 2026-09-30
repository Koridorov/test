def whole_check(num) -> bool:
    """This checks whether the number is whole or not"""
    if (num is float) or (num<=0):
        print("Please input a whole number. ")
        return False

def binarise(number:int) -> int:
    """Returns the entered number as binary"""
    if whole_check(number)!=False and number<1000:
        if number==0:
            return "0"
        if number==1:
            return "1"
        return binarise(number//2)+str(number%2)

print(binarise(123))