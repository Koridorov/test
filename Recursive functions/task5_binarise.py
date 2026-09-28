def whole_check(num):
    """This checks whether the number is whole or not"""
    if (num is float) or (num<=0):
        print("Please input a whole number. ")
        return False

def binarise(number:int):
    if whole_check(number)!=False:
        if number==0:
            return "0"
        if number==1:
            return "1"
        return binarise(number//2)+str(number%2)

print(binarise(123))